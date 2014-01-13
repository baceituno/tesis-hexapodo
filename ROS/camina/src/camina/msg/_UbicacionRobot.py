"""autogenerated by genpy from camina/UbicacionRobot.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class UbicacionRobot(genpy.Message):
  _md5sum = "18b8e62dc570df8f73add24bcd8323b4"
  _type = "camina/UbicacionRobot"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# Este mensaje contiene toda la informacion de la ubicacion
# del robot en el espacio
# Las dimensiones se manejan en metros

#Cuerpo
float32 coordenadaCuerpo_x
float32 coordenadaCuerpo_y
float32 coordenadaCuerpo_z
float32 orientacionCuerpo_roll
float32 orientacionCuerpo_pitch
float32 orientacionCuerpo_yaw
float32 velocidadCuerpo_x
float32 velocidadCuerpo_y
float32 velocidadCuerpo_z
#patas
uint8 NPata
float32[] coordenadaPata_x
float32[] coordenadaPata_y
float32[] coordenadaPata_z
float32[] coordenadaPataSistemaPata_x
float32[] coordenadaPataSistemaPata_y
float32[] coordenadaPataSistemaPata_z
float32[] coordenadaMotor1Pata_x
float32[] coordenadaMotor1Pata_y
float32[] coordenadaMotor1Pata_z
#fuerza patas
float32[]  pataTipFuerza_x
float32[]  pataTipFuerza_y
float32[]  pataTipFuerza_z
uint8[]  pataApoyo
#Centro de Masa
float32 centroMasaCuerpo_x
float32 centroMasaCuerpo_y
float32 centroMasaCuerpo_z
float32[] centroMasaPata_x
float32[] centroMasaPata_y
float32[] centroMasaPata_z

"""
  __slots__ = ['coordenadaCuerpo_x','coordenadaCuerpo_y','coordenadaCuerpo_z','orientacionCuerpo_roll','orientacionCuerpo_pitch','orientacionCuerpo_yaw','velocidadCuerpo_x','velocidadCuerpo_y','velocidadCuerpo_z','NPata','coordenadaPata_x','coordenadaPata_y','coordenadaPata_z','coordenadaPataSistemaPata_x','coordenadaPataSistemaPata_y','coordenadaPataSistemaPata_z','coordenadaMotor1Pata_x','coordenadaMotor1Pata_y','coordenadaMotor1Pata_z','pataTipFuerza_x','pataTipFuerza_y','pataTipFuerza_z','pataApoyo','centroMasaCuerpo_x','centroMasaCuerpo_y','centroMasaCuerpo_z','centroMasaPata_x','centroMasaPata_y','centroMasaPata_z']
  _slot_types = ['float32','float32','float32','float32','float32','float32','float32','float32','float32','uint8','float32[]','float32[]','float32[]','float32[]','float32[]','float32[]','float32[]','float32[]','float32[]','float32[]','float32[]','float32[]','uint8[]','float32','float32','float32','float32[]','float32[]','float32[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       coordenadaCuerpo_x,coordenadaCuerpo_y,coordenadaCuerpo_z,orientacionCuerpo_roll,orientacionCuerpo_pitch,orientacionCuerpo_yaw,velocidadCuerpo_x,velocidadCuerpo_y,velocidadCuerpo_z,NPata,coordenadaPata_x,coordenadaPata_y,coordenadaPata_z,coordenadaPataSistemaPata_x,coordenadaPataSistemaPata_y,coordenadaPataSistemaPata_z,coordenadaMotor1Pata_x,coordenadaMotor1Pata_y,coordenadaMotor1Pata_z,pataTipFuerza_x,pataTipFuerza_y,pataTipFuerza_z,pataApoyo,centroMasaCuerpo_x,centroMasaCuerpo_y,centroMasaCuerpo_z,centroMasaPata_x,centroMasaPata_y,centroMasaPata_z

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(UbicacionRobot, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.coordenadaCuerpo_x is None:
        self.coordenadaCuerpo_x = 0.
      if self.coordenadaCuerpo_y is None:
        self.coordenadaCuerpo_y = 0.
      if self.coordenadaCuerpo_z is None:
        self.coordenadaCuerpo_z = 0.
      if self.orientacionCuerpo_roll is None:
        self.orientacionCuerpo_roll = 0.
      if self.orientacionCuerpo_pitch is None:
        self.orientacionCuerpo_pitch = 0.
      if self.orientacionCuerpo_yaw is None:
        self.orientacionCuerpo_yaw = 0.
      if self.velocidadCuerpo_x is None:
        self.velocidadCuerpo_x = 0.
      if self.velocidadCuerpo_y is None:
        self.velocidadCuerpo_y = 0.
      if self.velocidadCuerpo_z is None:
        self.velocidadCuerpo_z = 0.
      if self.NPata is None:
        self.NPata = 0
      if self.coordenadaPata_x is None:
        self.coordenadaPata_x = []
      if self.coordenadaPata_y is None:
        self.coordenadaPata_y = []
      if self.coordenadaPata_z is None:
        self.coordenadaPata_z = []
      if self.coordenadaPataSistemaPata_x is None:
        self.coordenadaPataSistemaPata_x = []
      if self.coordenadaPataSistemaPata_y is None:
        self.coordenadaPataSistemaPata_y = []
      if self.coordenadaPataSistemaPata_z is None:
        self.coordenadaPataSistemaPata_z = []
      if self.coordenadaMotor1Pata_x is None:
        self.coordenadaMotor1Pata_x = []
      if self.coordenadaMotor1Pata_y is None:
        self.coordenadaMotor1Pata_y = []
      if self.coordenadaMotor1Pata_z is None:
        self.coordenadaMotor1Pata_z = []
      if self.pataTipFuerza_x is None:
        self.pataTipFuerza_x = []
      if self.pataTipFuerza_y is None:
        self.pataTipFuerza_y = []
      if self.pataTipFuerza_z is None:
        self.pataTipFuerza_z = []
      if self.pataApoyo is None:
        self.pataApoyo = ''
      if self.centroMasaCuerpo_x is None:
        self.centroMasaCuerpo_x = 0.
      if self.centroMasaCuerpo_y is None:
        self.centroMasaCuerpo_y = 0.
      if self.centroMasaCuerpo_z is None:
        self.centroMasaCuerpo_z = 0.
      if self.centroMasaPata_x is None:
        self.centroMasaPata_x = []
      if self.centroMasaPata_y is None:
        self.centroMasaPata_y = []
      if self.centroMasaPata_z is None:
        self.centroMasaPata_z = []
    else:
      self.coordenadaCuerpo_x = 0.
      self.coordenadaCuerpo_y = 0.
      self.coordenadaCuerpo_z = 0.
      self.orientacionCuerpo_roll = 0.
      self.orientacionCuerpo_pitch = 0.
      self.orientacionCuerpo_yaw = 0.
      self.velocidadCuerpo_x = 0.
      self.velocidadCuerpo_y = 0.
      self.velocidadCuerpo_z = 0.
      self.NPata = 0
      self.coordenadaPata_x = []
      self.coordenadaPata_y = []
      self.coordenadaPata_z = []
      self.coordenadaPataSistemaPata_x = []
      self.coordenadaPataSistemaPata_y = []
      self.coordenadaPataSistemaPata_z = []
      self.coordenadaMotor1Pata_x = []
      self.coordenadaMotor1Pata_y = []
      self.coordenadaMotor1Pata_z = []
      self.pataTipFuerza_x = []
      self.pataTipFuerza_y = []
      self.pataTipFuerza_z = []
      self.pataApoyo = ''
      self.centroMasaCuerpo_x = 0.
      self.centroMasaCuerpo_y = 0.
      self.centroMasaCuerpo_z = 0.
      self.centroMasaPata_x = []
      self.centroMasaPata_y = []
      self.centroMasaPata_z = []

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_9fB.pack(_x.coordenadaCuerpo_x, _x.coordenadaCuerpo_y, _x.coordenadaCuerpo_z, _x.orientacionCuerpo_roll, _x.orientacionCuerpo_pitch, _x.orientacionCuerpo_yaw, _x.velocidadCuerpo_x, _x.velocidadCuerpo_y, _x.velocidadCuerpo_z, _x.NPata))
      length = len(self.coordenadaPata_x)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.coordenadaPata_x))
      length = len(self.coordenadaPata_y)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.coordenadaPata_y))
      length = len(self.coordenadaPata_z)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.coordenadaPata_z))
      length = len(self.coordenadaPataSistemaPata_x)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.coordenadaPataSistemaPata_x))
      length = len(self.coordenadaPataSistemaPata_y)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.coordenadaPataSistemaPata_y))
      length = len(self.coordenadaPataSistemaPata_z)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.coordenadaPataSistemaPata_z))
      length = len(self.coordenadaMotor1Pata_x)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.coordenadaMotor1Pata_x))
      length = len(self.coordenadaMotor1Pata_y)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.coordenadaMotor1Pata_y))
      length = len(self.coordenadaMotor1Pata_z)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.coordenadaMotor1Pata_z))
      length = len(self.pataTipFuerza_x)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.pataTipFuerza_x))
      length = len(self.pataTipFuerza_y)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.pataTipFuerza_y))
      length = len(self.pataTipFuerza_z)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.pataTipFuerza_z))
      _x = self.pataApoyo
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3f.pack(_x.centroMasaCuerpo_x, _x.centroMasaCuerpo_y, _x.centroMasaCuerpo_z))
      length = len(self.centroMasaPata_x)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.centroMasaPata_x))
      length = len(self.centroMasaPata_y)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.centroMasaPata_y))
      length = len(self.centroMasaPata_z)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.centroMasaPata_z))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 37
      (_x.coordenadaCuerpo_x, _x.coordenadaCuerpo_y, _x.coordenadaCuerpo_z, _x.orientacionCuerpo_roll, _x.orientacionCuerpo_pitch, _x.orientacionCuerpo_yaw, _x.velocidadCuerpo_x, _x.velocidadCuerpo_y, _x.velocidadCuerpo_z, _x.NPata,) = _struct_9fB.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.coordenadaPata_x = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.coordenadaPata_y = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.coordenadaPata_z = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.coordenadaPataSistemaPata_x = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.coordenadaPataSistemaPata_y = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.coordenadaPataSistemaPata_z = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.coordenadaMotor1Pata_x = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.coordenadaMotor1Pata_y = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.coordenadaMotor1Pata_z = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.pataTipFuerza_x = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.pataTipFuerza_y = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.pataTipFuerza_z = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.pataApoyo = str[start:end].decode('utf-8')
      else:
        self.pataApoyo = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.centroMasaCuerpo_x, _x.centroMasaCuerpo_y, _x.centroMasaCuerpo_z,) = _struct_3f.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.centroMasaPata_x = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.centroMasaPata_y = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.centroMasaPata_z = struct.unpack(pattern, str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_9fB.pack(_x.coordenadaCuerpo_x, _x.coordenadaCuerpo_y, _x.coordenadaCuerpo_z, _x.orientacionCuerpo_roll, _x.orientacionCuerpo_pitch, _x.orientacionCuerpo_yaw, _x.velocidadCuerpo_x, _x.velocidadCuerpo_y, _x.velocidadCuerpo_z, _x.NPata))
      length = len(self.coordenadaPata_x)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.coordenadaPata_x.tostring())
      length = len(self.coordenadaPata_y)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.coordenadaPata_y.tostring())
      length = len(self.coordenadaPata_z)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.coordenadaPata_z.tostring())
      length = len(self.coordenadaPataSistemaPata_x)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.coordenadaPataSistemaPata_x.tostring())
      length = len(self.coordenadaPataSistemaPata_y)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.coordenadaPataSistemaPata_y.tostring())
      length = len(self.coordenadaPataSistemaPata_z)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.coordenadaPataSistemaPata_z.tostring())
      length = len(self.coordenadaMotor1Pata_x)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.coordenadaMotor1Pata_x.tostring())
      length = len(self.coordenadaMotor1Pata_y)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.coordenadaMotor1Pata_y.tostring())
      length = len(self.coordenadaMotor1Pata_z)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.coordenadaMotor1Pata_z.tostring())
      length = len(self.pataTipFuerza_x)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.pataTipFuerza_x.tostring())
      length = len(self.pataTipFuerza_y)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.pataTipFuerza_y.tostring())
      length = len(self.pataTipFuerza_z)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.pataTipFuerza_z.tostring())
      _x = self.pataApoyo
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3f.pack(_x.centroMasaCuerpo_x, _x.centroMasaCuerpo_y, _x.centroMasaCuerpo_z))
      length = len(self.centroMasaPata_x)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.centroMasaPata_x.tostring())
      length = len(self.centroMasaPata_y)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.centroMasaPata_y.tostring())
      length = len(self.centroMasaPata_z)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.centroMasaPata_z.tostring())
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 37
      (_x.coordenadaCuerpo_x, _x.coordenadaCuerpo_y, _x.coordenadaCuerpo_z, _x.orientacionCuerpo_roll, _x.orientacionCuerpo_pitch, _x.orientacionCuerpo_yaw, _x.velocidadCuerpo_x, _x.velocidadCuerpo_y, _x.velocidadCuerpo_z, _x.NPata,) = _struct_9fB.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.coordenadaPata_x = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.coordenadaPata_y = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.coordenadaPata_z = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.coordenadaPataSistemaPata_x = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.coordenadaPataSistemaPata_y = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.coordenadaPataSistemaPata_z = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.coordenadaMotor1Pata_x = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.coordenadaMotor1Pata_y = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.coordenadaMotor1Pata_z = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.pataTipFuerza_x = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.pataTipFuerza_y = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.pataTipFuerza_z = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.pataApoyo = str[start:end].decode('utf-8')
      else:
        self.pataApoyo = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.centroMasaCuerpo_x, _x.centroMasaCuerpo_y, _x.centroMasaCuerpo_z,) = _struct_3f.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.centroMasaPata_x = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.centroMasaPata_y = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.centroMasaPata_z = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_3f = struct.Struct("<3f")
_struct_9fB = struct.Struct("<9fB")