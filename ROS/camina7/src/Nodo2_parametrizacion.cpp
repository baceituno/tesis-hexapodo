#include "ros/ros.h"
#include "math.h"
#include "string.h"
//Librerias propias usadas
#include "constantes.hpp"
#include "camina7/v_repConst.h"
// Used data structures:
#include "camina7/DatosTrayectoriaPata.h"
#include "camina7/AngulosMotor.h"
#include "camina7/CinversaParametros.h"
#include "camina7/TransHomogeneaParametros.h"
// Used API services:
#include "vrep_common/VrepInfo.h"
//Definiciones
//#define TrayInicio -0.05
//Clientes y Servicios
ros::ServiceClient client_Cinversa;
camina7::CinversaParametros srv_Cinversa;
ros::ServiceClient client_TransHomogenea;
camina7::TransHomogeneaParametros srv_TransHomogenea;

//-- Global variables (modified by topic subscribers):
bool simulationRunning=true;
bool sensorTrigger=false;
float simulationTime=0.0f;
int Npata_arg=0, Tripode=0, Estado=0, prevEstado=0;
bool Inicio=true;
//-- Calculo de trayectoria
float T=0.0, beta=0.0, lambda_Apoyo=0.0, lambda_Transferencia=0.0, dh=0.0, desfasaje_t=0.0, phi=0.0;
float x_S0=0.0, y_S0=0.0, z_S0=0.0;
float finTransferencia_x=0.0, finApoyo_x;
float x_Offset=0.0, y_Offset=0.0, z_Offset=0.0;   //matriz de transformacion homogenea
camina7::AngulosMotor qMotor;
ros::Publisher chatter_pub;
FILE *fp1;
//-- Funciones
void Trayectoria_FaseApoyo(float t_Trayectoria,float PuntoInicio_x,float PuntoInicio_y,float PuntoInicio_z);
void Trayectoria_FaseTrans_Eliptica(float t_Trayectoria,float PuntoInicio_x,float PuntoInicio_y,float PuntoInicio_z);

// Topic subscriber callbacks:
void infoCallback(const vrep_common::VrepInfo::ConstPtr& info)
{
	simulationTime=info->simulationTime.data;
	simulationRunning=(info->simulatorState.data&1)!=0;
}

/* Callback que escucha el topico DatosDeTrayectoria calcula la trayectoria
   deseaday cinematica inversa para de motores y los publica
*/
void datosCallback(const camina7::DatosTrayectoriaPata msg_datoTrayectoria)
{
    float t_Trayectoria=0.0;
    float alfa=0.0;
    float x_S1=0.0, y_S1=0.0, z_S1=0.0;
    float PuntoInicio_x=0.0, PuntoInicio_y=0.0, PuntoInicio_z=0.0;

    T = msg_datoTrayectoria.T_apoyo[Tripode-1];
	t_Trayectoria = msg_datoTrayectoria.t_Trayectoria[Tripode-1];
    lambda_Apoyo = msg_datoTrayectoria.lambda_Apoyo[Tripode-1];
    lambda_Transferencia = msg_datoTrayectoria.lambda_Transferencia[Tripode-1];
    alfa = msg_datoTrayectoria.alfa[Tripode-1];
    desfasaje_t = msg_datoTrayectoria.desfasaje_t[Tripode-1];
    Estado = msg_datoTrayectoria.vector_estados[Tripode-1];

//    if(prevEstado>Estado){
//    //--- Se pasa de estado de transferencia a estado de apoyo
//    //--- inicia apoyo
////        finTransferencia_x = x_S0;
//        finTransferencia_x = (y_Offset-FinEspacioTrabajo_y)-lambda_Apoyo;
//    }

    //---------------------------------
//    if (Inicio){
//    //-- La trayectoria inicial se hace con lambda de apoyo
//        Inicio = false;
//        lambda_Apoyo = lambda_Transferencia;
//        finTransferencia_x = (y_Offset-FinEspacioTrabajo_y)-lambda_Apoyo;
//        finApoyo_x = (y_Offset-FinEspacioTrabajo_y)-lambda_Transferencia/2;
//    }

    //-----Parametrizacion de trayectoria eliptica en Sistema de Robot
    // Periodo A-B
    if (Estado==Apoyo)
    {
    //---Apoyo------
//        PuntoInicio_x=finTransferencia_x;
        PuntoInicio_x=(y_Offset-FinEspacioTrabajo_y)-lambda_Apoyo;
        PuntoInicio_y=0.0;
        PuntoInicio_z=0.0;
        Trayectoria_FaseApoyo(t_Trayectoria,PuntoInicio_x,PuntoInicio_y,PuntoInicio_z);
    } else {
    //---Transferencia------
    // Elipsis
//        PuntoInicio_x=(y_Offset-FinEspacioTrabajo_y)-lambda_Transferencia/2;
        PuntoInicio_x=(y_Offset-FinEspacioTrabajo_y)-lambda_Transferencia/2;
        PuntoInicio_y=0.0;
        PuntoInicio_z=0.0;
        Trayectoria_FaseTrans_Eliptica(t_Trayectoria,PuntoInicio_x,PuntoInicio_y,PuntoInicio_z);
    }

//    prevEstado = Estado;
    //-----Transformacion de trayectoria a Sistema de Pata
    x_S1 = x_Offset + x_S0*cos(phi+alfa) - y_S0*sin(phi+alfa);
    y_S1 = y_Offset + x_S0*sin(phi+alfa) + y_S0*cos(phi+alfa);
    z_S1 = z_Offset + z_S0;
    //-----Cinematica Inversa
    srv_Cinversa.request.x = x_S1;
    srv_Cinversa.request.y = y_S1;
    srv_Cinversa.request.z = z_S1;

    if (client_Cinversa.call(srv_Cinversa)&&(srv_Cinversa.response.result!=-1))
    {   qMotor.q1 = srv_Cinversa.response.q1;
        qMotor.q2 = srv_Cinversa.response.q2;
        qMotor.q3 = srv_Cinversa.response.q3;
    } else {
        ROS_ERROR("Nodo 2::[%d] servicio de Cinversa no funciona\n",Npata_arg);
//        return;
    }

    fprintf(fp1,"%.3f,%.3f,%.3f,%.3f,%.3f,%.3f,%.3f\n",qMotor.q1,qMotor.q2,qMotor.q3,t_Trayectoria,x_S1,y_S1,z_S1);
    //---Publica angulos motores----
    qMotor.Npata = Npata_arg;
	chatter_pub.publish(qMotor);
}

int main(int argc, char **argv){

	if (argc>=8)
	{
		Npata_arg=atoi(argv[1]);
		dh=atof(argv[2]);
        x_Offset=atof(argv[3]);
        y_Offset=atof(argv[4]);
        z_Offset=atof(argv[5]);
        phi=atof(argv[6])*pi/180.0;
        Tripode=atof(argv[7]);
	}
	else
	{
		ROS_ERROR("Nodo 2::[%d] Indique argumentos!\n",Npata_arg);
		sleep(5000);
		return 0;
	}

    /*Inicio nodo de ROS*/
    std::string nodeName("Nodo2_Parametrizacion_pata");
	std::string Id(boost::lexical_cast<std::string>(Npata_arg));
	nodeName+=Id;
	ros::init(argc,argv,nodeName.c_str());
    ros::NodeHandle node;
    //ROS_INFO("Nodo2_Parametrizacion just started\n");

//-- Topicos susbcritos y publicados
    chatter_pub = node.advertise<camina7::AngulosMotor>("DatosDeMotores", 100);
    ros::Subscriber subInfo = node.subscribe("/vrep/info",1,infoCallback);
//-- Recibe topico especifico
    ros::Subscriber sub = node.subscribe("datosTrayectoria", 100, datosCallback);
//-- Clientes y Servicios
    client_Cinversa = node.serviceClient<camina7::CinversaParametros>("Cinversa");
    client_TransHomogenea = node.serviceClient<camina7::TransHomogeneaParametros>("TransHomogenea");

    std::string fileName("../fuerte_workspace/sandbox/TesisMaureen/ROS/camina7/datos/QXEnviada_Pata");
    std::string texto(".txt");
    fileName+=Id;
    fileName+=texto;
    fp1 = fopen(fileName.c_str(),"w+");

    while (ros::ok() && simulationRunning)
    {
	  ros::spinOnce();
    }
    fclose(fp1);
    //ROS_INFO("Adios2!");
    ros::shutdown();
    return 0;
}

//---Caso parte 1 trayectoria----
//-- Periodo A-B
void Trayectoria_FaseApoyo(float t_Trayectoria,float PuntoInicio_x,float PuntoInicio_y,float PuntoInicio_z){

    float velocidadApoyo=0.0;

    velocidadApoyo = lambda_Apoyo/T;

    x_S0 = PuntoInicio_x + velocidadApoyo*t_Trayectoria;
    y_S0 = PuntoInicio_y;
    z_S0 = PuntoInicio_z;
//    if (fabs(t_Trayectoria-beta*T)<2*(delta_t)){
//        ROS_INFO("[%d] fin apoyo",Npata_arg);
//    }
}

//---Caso parte 2 trayectoria----
//-- Elipsis
void Trayectoria_FaseTrans_Eliptica(float t_Trayectoria,float PuntoInicio_x,float PuntoInicio_y,float PuntoInicio_z){

    float theta=0.0, t_aux=0.0;

    t_aux = t_Trayectoria/T;
    theta = pi*t_aux;

    x_S0 = PuntoInicio_x + (lambda_Transferencia/2)*cos(theta);
    y_S0 = PuntoInicio_y;
    z_S0 = PuntoInicio_z + dh*sin(theta);
}
