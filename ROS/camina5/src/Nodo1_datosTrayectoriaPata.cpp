#include "ros/ros.h"
#include "std_msgs/String.h"
#include "math.h"
//Librerias propias usadas
#include "constantes.hpp"
#include "camina5/v_repConst.h"
// Used data structures:
#include "camina5/DatosTrayectoriaPata.h"
#include "camina5/PlanificadorParametros.h"
#include "camina5/SenalesCambios.h"
// Used API services:
#include "vrep_common/VrepInfo.h"
//Clientes y Servicios
ros::ServiceClient client_Planificador;
camina5::PlanificadorParametros srv_Planificador;

// variables Globales
bool simulationRunning=true;
bool sensorTrigger=false;
float simulationTime=0.0f;
camina5::DatosTrayectoriaPata datosTrayectoriaPata_T1, datosTrayectoriaPata_T2;
float divisionTrayectoriaPata=0.0, T=0.0, lambda_Transferencia=0.0, divisionTiempo=0.0, desfasaje_t_T1=0.0,desfasaje_t_T2=0.0, beta=0.0;
float modificacion_T = 0.0, modificacion_lambda =0.0;
bool InicioApoyo_T1=false, FinApoyo_T1=false, InicioApoyo_T2=false, FinApoyo_T2=false, cambioPlan=false;
float delta_t=0.0, t_aux_T1=0.0,t_aux_T2=0.0;
FILE *fp1;
ros::Publisher chatter_pub1,chatter_pub2;

// Funciones
bool LlamadaPlanificador_T1(float t_actual);
bool LlamadaPlanificador_T2(float t_actual);
// Topic subscriber callbacks:
void infoCallback(const vrep_common::VrepInfo::ConstPtr& info)
{
	simulationTime=info->simulationTime.data;
	simulationRunning=(info->simulatorState.data&1)!=0;
}

void relojCallback(camina5::SenalesCambios msgSenal)
{
    if (!msgSenal.Stop){

        cambioPlan=false;
        //------- T1 --------------------
        t_aux_T1=delta_t+desfasaje_t_T1*T;
        t_aux_T1=fmod(t_aux_T1,T);
        cambioPlan = LlamadaPlanificador_T1(t_aux_T1);
        //-------------------------------
        //------- T2 --------------------
        t_aux_T2=delta_t+desfasaje_t_T2*T;
        t_aux_T2=fmod(t_aux_T2,T);
//        cambioPlan = LlamadaPlanificador_T2(t_aux_T2);
        //-------------------------------
        if(cambioPlan){
            T = modificacion_T;
            divisionTrayectoriaPata = T/divisionTiempo;
            //-- datos a enviar
            datosTrayectoriaPata_T1.T = modificacion_T;
            datosTrayectoriaPata_T1.lambda_Transferencia = modificacion_lambda;
            datosTrayectoriaPata_T1.divisionTrayectoriaPata=divisionTrayectoriaPata;
            datosTrayectoriaPata_T2.T = modificacion_T;
            datosTrayectoriaPata_T2.lambda_Transferencia = modificacion_lambda;
            datosTrayectoriaPata_T2.divisionTrayectoriaPata = divisionTrayectoriaPata;
            cambioPlan = false;
        }

//        if (fabs(delta_t-T)<=(T/divisionTrayectoriaPata)) {
////            ROS_INFO("reinicio trayectoria[%d]",Tripode);
//            delta_t = 0.0;
////            t_aux = 0.0;
//        }

        datosTrayectoriaPata_T1.t_Trayectoria = t_aux_T1;
        datosTrayectoriaPata_T2.t_Trayectoria = t_aux_T2;
        //-- Esta linea es muy importante
        chatter_pub1.publish(datosTrayectoriaPata_T1);
        chatter_pub2.publish(datosTrayectoriaPata_T2);

        delta_t = delta_t + T/divisionTrayectoriaPata;

        if (fabs(delta_t-T)<=(T/divisionTrayectoriaPata)) {
//            ROS_INFO("reinicio trayectoria[%d]",Tripode);
            delta_t = 0.0;
//            t_aux = 0.0;
        }
    }
}

int main(int argc, char **argv)
{
  float lambda_Apoyo=0.0, alfa=0.0, f=0.0;
  int i=0, Narg=0;

  Narg=8;
	if (argc>=Narg)
	{
        T=atof(argv[1]); // Periodo de trayectoria [seg]
		divisionTrayectoriaPata=atof(argv[2]);  //N puntos
		beta=atof(argv[3]);
		lambda_Apoyo=atof(argv[4]);
		lambda_Transferencia=atof(argv[5]);
		alfa=atof(argv[6])*pi/180;
        desfasaje_t_T1=atof(argv[7]);
        desfasaje_t_T2=atof(argv[8]);
    } else {
		ROS_ERROR("Nodo1: Indique argumentos!\n");
		return 0;
	}

	/*Inicio nodo de ROS*/
    std::string nodeName("Nodo1_datosTrayectoriaPata");
	ros::init(argc,argv,nodeName.c_str());
    ros::NodeHandle node;

//-- Topicos susbcritos y publicados
    ros::Subscriber subInfo1=node.subscribe("/vrep/info",100,infoCallback);
    ros::Subscriber subInfo2=node.subscribe("Reloj",100,relojCallback);
//-- Manda topico especifico para cada pata
    chatter_pub1=node.advertise<camina5::DatosTrayectoriaPata>("datosTrayectoria_T1", 100);
    chatter_pub2=node.advertise<camina5::DatosTrayectoriaPata>("datosTrayectoria_T2", 100);
//-- Clientes y Servicios
    client_Planificador = node.serviceClient<camina5::PlanificadorParametros>("PlanificadorPisada");
//-- Log de datos
//    std::string fileName("../fuerte_workspace/sandbox/TesisMaureen/ROS/camina5/datos/SalidaDatos");
//    std::string texto(".txt");
//    fileName+=Id;
//    fileName+=texto;
//    fp1 = fopen(fileName.c_str(),"w+");

//-- Datos de envio
    datosTrayectoriaPata_T1.T=T;
    datosTrayectoriaPata_T1.divisionTrayectoriaPata=divisionTrayectoriaPata;
    datosTrayectoriaPata_T1.lambda_Apoyo=lambda_Apoyo;
    datosTrayectoriaPata_T1.lambda_Transferencia=lambda_Transferencia;
    datosTrayectoriaPata_T1.alfa=alfa;
    datosTrayectoriaPata_T1.desfasaje_t=desfasaje_t_T1;
    //-----------------------------------------------------------------
    datosTrayectoriaPata_T2.T=T;
    datosTrayectoriaPata_T2.divisionTrayectoriaPata=divisionTrayectoriaPata;
    datosTrayectoriaPata_T2.lambda_Apoyo=lambda_Apoyo;
    datosTrayectoriaPata_T2.lambda_Transferencia=lambda_Transferencia;
    datosTrayectoriaPata_T2.alfa=alfa;
    datosTrayectoriaPata_T2.desfasaje_t=desfasaje_t_T2;

//-- Prepara variables para calculos de trayectoria de PATA
    //delta_t = 1/divisionTrayectoriaPata;
    divisionTiempo = T/divisionTrayectoriaPata;
    f=1/divisionTiempo;
    /* La velocidad de envío de los datos se encarga de darme el tiempo total de trayectoria deseado */
    /* Velocidad de transmision */
    ros::Rate loop_rate(f);  //Frecuencia [Hz]
//-- Delay inicial para esperar inicio de todos los nodos
    for(i=0;i<10;i++) loop_rate.sleep();

    modificacion_T = T;
    modificacion_lambda = lambda_Transferencia;

    while (ros::ok() && simulationRunning){
        ros::spinOnce();
//        loop_rate.sleep();
    }
        ROS_INFO("Adios1!");
//        fclose(fp1);
        ros::shutdown();
        return 0;
    }


/* Funciones */

bool LlamadaPlanificador_T1(float t_actual){
    int Tripode = T1;
    bool salidaPlan = false;

    if (t_actual<2*(T/divisionTrayectoriaPata) and FinApoyo_T1) {
        InicioApoyo_T1=true;
        FinApoyo_T1=false;
    }
    if (fabs(t_actual-beta*T)<2*(T/divisionTrayectoriaPata)) {
        FinApoyo_T1=true;
    }

    if (InicioApoyo_T1){
        InicioApoyo_T1=false;
        srv_Planificador.request.Tripode = Tripode;
        srv_Planificador.request.T = T;
        if (client_Planificador.call(srv_Planificador)){
            modificacion_lambda = srv_Planificador.response.modificacion_lambda;
            modificacion_T = srv_Planificador.response.modificacion_T;
            ROS_INFO("Nodo1::T[%d]: t_sim=%.3f, t_actual=%.3f, lambda_c=%.3f,t_c=%.3f",Tripode,simulationTime,t_actual,modificacion_lambda,modificacion_T);
            salidaPlan = true;
        } else {
            ROS_ERROR("Nodo1::T[%d] servicio de Planificacion no funciona",Tripode);
            ROS_ERROR("result=%d", srv_Planificador.response.result);
        }
    }
    return salidaPlan;
}

bool LlamadaPlanificador_T2(float t_actual){
    int Tripode = T2;
    bool salidaPlan = false;

    if (t_actual<2*(T/divisionTrayectoriaPata) and FinApoyo_T2) {
        InicioApoyo_T2=true;
        FinApoyo_T2=false;
    }
    if (fabs(t_actual-beta*T)<2*(T/divisionTrayectoriaPata)) {
        FinApoyo_T2=true;
    }

    if (InicioApoyo_T2){
        InicioApoyo_T2=false;
        srv_Planificador.request.Tripode = Tripode;
        srv_Planificador.request.T = T;
        if (client_Planificador.call(srv_Planificador)){
            modificacion_lambda = srv_Planificador.response.modificacion_lambda;
            modificacion_T = srv_Planificador.response.modificacion_T;
            ROS_INFO("Nodo1::T[%d]: t_sim=%.3f, t_actual=%.3f, lambda_c=%.3f,t_c=%.3f",Tripode,simulationTime,t_actual,modificacion_lambda,modificacion_T);
            salidaPlan = true;
        } else {
            ROS_ERROR("Nodo1::T[%d] servicio de Planificacion no funciona",Tripode);
            ROS_ERROR("result=%d", srv_Planificador.response.result);
        }
    }
    return salidaPlan;
}
