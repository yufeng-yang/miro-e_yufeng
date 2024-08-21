# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from miro2_msg/objects.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import miro2_msg.msg

class objects(genpy.Message):
  _md5sum = "0751afb21e15f80b448531e265b3963f"
  _type = "miro2_msg/objects"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """#	@section COPYRIGHT
#	Copyright (C) 2023 Consequential Robotics Ltd
#	
#	@section AUTHOR
#	Consequential Robotics http://consequentialrobotics.com
#	
#	@section LICENSE
#	For a full copy of the license agreement, and a complete
#	definition of "The Software", see LICENSE in the MDK root
#	directory.
#	
#	Subject to the terms of this Agreement, Consequential
#	Robotics grants to you a limited, non-exclusive, non-
#	transferable license, without right to sub-license, to use
#	"The Software" in accordance with this Agreement and any
#	other written agreement with Consequential Robotics.
#	Consequential Robotics does not transfer the title of "The
#	Software" to you; the license granted to you is not a sale.
#	This agreement is a binding legal agreement between
#	Consequential Robotics and the purchasers or users of "The
#	Software".
#	
#	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
#	KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
#	WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
#	PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
#	OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
#	OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
#	OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
#	SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#	

# header
int32 stream_index

#	objects
object_tag[] tags
object_ball[] balls
object_face[] faces


================================================================================
MSG: miro2_msg/object_tag
#	@section COPYRIGHT
#	Copyright (C) 2023 Consequential Robotics Ltd
#	
#	@section AUTHOR
#	Consequential Robotics http://consequentialrobotics.com
#	
#	@section LICENSE
#	For a full copy of the license agreement, and a complete
#	definition of "The Software", see LICENSE in the MDK root
#	directory.
#	
#	Subject to the terms of this Agreement, Consequential
#	Robotics grants to you a limited, non-exclusive, non-
#	transferable license, without right to sub-license, to use
#	"The Software" in accordance with this Agreement and any
#	other written agreement with Consequential Robotics.
#	Consequential Robotics does not transfer the title of "The
#	Software" to you; the license granted to you is not a sale.
#	This agreement is a binding legal agreement between
#	Consequential Robotics and the purchasers or users of "The
#	Software".
#	
#	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
#	KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
#	WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
#	PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
#	OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
#	OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
#	OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
#	SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#	

float32 conf
int32 id
float32[2] centre
float32[8] corners


================================================================================
MSG: miro2_msg/object_ball
#	@section COPYRIGHT
#	Copyright (C) 2023 Consequential Robotics Ltd
#	
#	@section AUTHOR
#	Consequential Robotics http://consequentialrobotics.com
#	
#	@section LICENSE
#	For a full copy of the license agreement, and a complete
#	definition of "The Software", see LICENSE in the MDK root
#	directory.
#	
#	Subject to the terms of this Agreement, Consequential
#	Robotics grants to you a limited, non-exclusive, non-
#	transferable license, without right to sub-license, to use
#	"The Software" in accordance with this Agreement and any
#	other written agreement with Consequential Robotics.
#	Consequential Robotics does not transfer the title of "The
#	Software" to you; the license granted to you is not a sale.
#	This agreement is a binding legal agreement between
#	Consequential Robotics and the purchasers or users of "The
#	Software".
#	
#	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
#	KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
#	WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
#	PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
#	OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
#	OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
#	OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
#	SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#	

float32 conf
float32[2] centre
float32 radius


================================================================================
MSG: miro2_msg/object_face
#	@section COPYRIGHT
#	Copyright (C) 2023 Consequential Robotics Ltd
#	
#	@section AUTHOR
#	Consequential Robotics http://consequentialrobotics.com
#	
#	@section LICENSE
#	For a full copy of the license agreement, and a complete
#	definition of "The Software", see LICENSE in the MDK root
#	directory.
#	
#	Subject to the terms of this Agreement, Consequential
#	Robotics grants to you a limited, non-exclusive, non-
#	transferable license, without right to sub-license, to use
#	"The Software" in accordance with this Agreement and any
#	other written agreement with Consequential Robotics.
#	Consequential Robotics does not transfer the title of "The
#	Software" to you; the license granted to you is not a sale.
#	This agreement is a binding legal agreement between
#	Consequential Robotics and the purchasers or users of "The
#	Software".
#	
#	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
#	KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
#	WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
#	PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
#	OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
#	OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
#	OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
#	SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#	

float32 conf
float32[2] corner
float32[2] size

"""
  __slots__ = ['stream_index','tags','balls','faces']
  _slot_types = ['int32','miro2_msg/object_tag[]','miro2_msg/object_ball[]','miro2_msg/object_face[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       stream_index,tags,balls,faces

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(objects, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.stream_index is None:
        self.stream_index = 0
      if self.tags is None:
        self.tags = []
      if self.balls is None:
        self.balls = []
      if self.faces is None:
        self.faces = []
    else:
      self.stream_index = 0
      self.tags = []
      self.balls = []
      self.faces = []

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
      _x = self.stream_index
      buff.write(_get_struct_i().pack(_x))
      length = len(self.tags)
      buff.write(_struct_I.pack(length))
      for val1 in self.tags:
        _x = val1
        buff.write(_get_struct_fi().pack(_x.conf, _x.id))
        buff.write(_get_struct_2f().pack(*val1.centre))
        buff.write(_get_struct_8f().pack(*val1.corners))
      length = len(self.balls)
      buff.write(_struct_I.pack(length))
      for val1 in self.balls:
        _x = val1.conf
        buff.write(_get_struct_f().pack(_x))
        buff.write(_get_struct_2f().pack(*val1.centre))
        _x = val1.radius
        buff.write(_get_struct_f().pack(_x))
      length = len(self.faces)
      buff.write(_struct_I.pack(length))
      for val1 in self.faces:
        _x = val1.conf
        buff.write(_get_struct_f().pack(_x))
        buff.write(_get_struct_2f().pack(*val1.corner))
        buff.write(_get_struct_2f().pack(*val1.size))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.tags is None:
        self.tags = None
      if self.balls is None:
        self.balls = None
      if self.faces is None:
        self.faces = None
      end = 0
      start = end
      end += 4
      (self.stream_index,) = _get_struct_i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.tags = []
      for i in range(0, length):
        val1 = miro2_msg.msg.object_tag()
        _x = val1
        start = end
        end += 8
        (_x.conf, _x.id,) = _get_struct_fi().unpack(str[start:end])
        start = end
        end += 8
        val1.centre = _get_struct_2f().unpack(str[start:end])
        start = end
        end += 32
        val1.corners = _get_struct_8f().unpack(str[start:end])
        self.tags.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.balls = []
      for i in range(0, length):
        val1 = miro2_msg.msg.object_ball()
        start = end
        end += 4
        (val1.conf,) = _get_struct_f().unpack(str[start:end])
        start = end
        end += 8
        val1.centre = _get_struct_2f().unpack(str[start:end])
        start = end
        end += 4
        (val1.radius,) = _get_struct_f().unpack(str[start:end])
        self.balls.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.faces = []
      for i in range(0, length):
        val1 = miro2_msg.msg.object_face()
        start = end
        end += 4
        (val1.conf,) = _get_struct_f().unpack(str[start:end])
        start = end
        end += 8
        val1.corner = _get_struct_2f().unpack(str[start:end])
        start = end
        end += 8
        val1.size = _get_struct_2f().unpack(str[start:end])
        self.faces.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.stream_index
      buff.write(_get_struct_i().pack(_x))
      length = len(self.tags)
      buff.write(_struct_I.pack(length))
      for val1 in self.tags:
        _x = val1
        buff.write(_get_struct_fi().pack(_x.conf, _x.id))
        buff.write(val1.centre.tostring())
        buff.write(val1.corners.tostring())
      length = len(self.balls)
      buff.write(_struct_I.pack(length))
      for val1 in self.balls:
        _x = val1.conf
        buff.write(_get_struct_f().pack(_x))
        buff.write(val1.centre.tostring())
        _x = val1.radius
        buff.write(_get_struct_f().pack(_x))
      length = len(self.faces)
      buff.write(_struct_I.pack(length))
      for val1 in self.faces:
        _x = val1.conf
        buff.write(_get_struct_f().pack(_x))
        buff.write(val1.corner.tostring())
        buff.write(val1.size.tostring())
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.tags is None:
        self.tags = None
      if self.balls is None:
        self.balls = None
      if self.faces is None:
        self.faces = None
      end = 0
      start = end
      end += 4
      (self.stream_index,) = _get_struct_i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.tags = []
      for i in range(0, length):
        val1 = miro2_msg.msg.object_tag()
        _x = val1
        start = end
        end += 8
        (_x.conf, _x.id,) = _get_struct_fi().unpack(str[start:end])
        start = end
        end += 8
        val1.centre = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=2)
        start = end
        end += 32
        val1.corners = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=8)
        self.tags.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.balls = []
      for i in range(0, length):
        val1 = miro2_msg.msg.object_ball()
        start = end
        end += 4
        (val1.conf,) = _get_struct_f().unpack(str[start:end])
        start = end
        end += 8
        val1.centre = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=2)
        start = end
        end += 4
        (val1.radius,) = _get_struct_f().unpack(str[start:end])
        self.balls.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.faces = []
      for i in range(0, length):
        val1 = miro2_msg.msg.object_face()
        start = end
        end += 4
        (val1.conf,) = _get_struct_f().unpack(str[start:end])
        start = end
        end += 8
        val1.corner = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=2)
        start = end
        end += 8
        val1.size = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=2)
        self.faces.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2f = None
def _get_struct_2f():
    global _struct_2f
    if _struct_2f is None:
        _struct_2f = struct.Struct("<2f")
    return _struct_2f
_struct_8f = None
def _get_struct_8f():
    global _struct_8f
    if _struct_8f is None:
        _struct_8f = struct.Struct("<8f")
    return _struct_8f
_struct_f = None
def _get_struct_f():
    global _struct_f
    if _struct_f is None:
        _struct_f = struct.Struct("<f")
    return _struct_f
_struct_fi = None
def _get_struct_fi():
    global _struct_fi
    if _struct_fi is None:
        _struct_fi = struct.Struct("<fi")
    return _struct_fi
_struct_i = None
def _get_struct_i():
    global _struct_i
    if _struct_i is None:
        _struct_i = struct.Struct("<i")
    return _struct_i
