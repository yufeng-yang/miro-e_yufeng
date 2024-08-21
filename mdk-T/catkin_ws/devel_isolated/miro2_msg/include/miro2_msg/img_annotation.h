// Generated by gencpp from file miro2_msg/img_annotation.msg
// DO NOT EDIT!


#ifndef MIRO2_MSG_MESSAGE_IMG_ANNOTATION_H
#define MIRO2_MSG_MESSAGE_IMG_ANNOTATION_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>
#include <std_msgs/String.h>
#include <std_msgs/String.h>
#include <std_msgs/Float32MultiArray.h>
#include <std_msgs/Float32MultiArray.h>
#include <std_msgs/Float32.h>
#include <std_msgs/Float32.h>
#include <std_msgs/UInt8.h>
#include <std_msgs/Float32.h>

namespace miro2_msg
{
template <class ContainerAllocator>
struct img_annotation_
{
  typedef img_annotation_<ContainerAllocator> Type;

  img_annotation_()
    : header()
    , type()
    , cam()
    , centre()
    , vertices()
    , size()
    , area()
    , id()
    , distance()  {
    }
  img_annotation_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , type(_alloc)
    , cam(_alloc)
    , centre(_alloc)
    , vertices(_alloc)
    , size(_alloc)
    , area(_alloc)
    , id(_alloc)
    , distance(_alloc)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef  ::std_msgs::String_<ContainerAllocator>  _type_type;
  _type_type type;

   typedef  ::std_msgs::String_<ContainerAllocator>  _cam_type;
  _cam_type cam;

   typedef  ::std_msgs::Float32MultiArray_<ContainerAllocator>  _centre_type;
  _centre_type centre;

   typedef  ::std_msgs::Float32MultiArray_<ContainerAllocator>  _vertices_type;
  _vertices_type vertices;

   typedef  ::std_msgs::Float32_<ContainerAllocator>  _size_type;
  _size_type size;

   typedef  ::std_msgs::Float32_<ContainerAllocator>  _area_type;
  _area_type area;

   typedef  ::std_msgs::UInt8_<ContainerAllocator>  _id_type;
  _id_type id;

   typedef  ::std_msgs::Float32_<ContainerAllocator>  _distance_type;
  _distance_type distance;





  typedef boost::shared_ptr< ::miro2_msg::img_annotation_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::miro2_msg::img_annotation_<ContainerAllocator> const> ConstPtr;

}; // struct img_annotation_

typedef ::miro2_msg::img_annotation_<std::allocator<void> > img_annotation;

typedef boost::shared_ptr< ::miro2_msg::img_annotation > img_annotationPtr;
typedef boost::shared_ptr< ::miro2_msg::img_annotation const> img_annotationConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::miro2_msg::img_annotation_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::miro2_msg::img_annotation_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::miro2_msg::img_annotation_<ContainerAllocator1> & lhs, const ::miro2_msg::img_annotation_<ContainerAllocator2> & rhs)
{
  return lhs.header == rhs.header &&
    lhs.type == rhs.type &&
    lhs.cam == rhs.cam &&
    lhs.centre == rhs.centre &&
    lhs.vertices == rhs.vertices &&
    lhs.size == rhs.size &&
    lhs.area == rhs.area &&
    lhs.id == rhs.id &&
    lhs.distance == rhs.distance;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::miro2_msg::img_annotation_<ContainerAllocator1> & lhs, const ::miro2_msg::img_annotation_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace miro2_msg

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::miro2_msg::img_annotation_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::miro2_msg::img_annotation_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::miro2_msg::img_annotation_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::miro2_msg::img_annotation_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::miro2_msg::img_annotation_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::miro2_msg::img_annotation_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::miro2_msg::img_annotation_<ContainerAllocator> >
{
  static const char* value()
  {
    return "7933292787df9dea2afeb186ff97727a";
  }

  static const char* value(const ::miro2_msg::img_annotation_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x7933292787df9deaULL;
  static const uint64_t static_value2 = 0x2afeb186ff97727aULL;
};

template<class ContainerAllocator>
struct DataType< ::miro2_msg::img_annotation_<ContainerAllocator> >
{
  static const char* value()
  {
    return "miro2_msg/img_annotation";
  }

  static const char* value(const ::miro2_msg::img_annotation_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::miro2_msg::img_annotation_<ContainerAllocator> >
{
  static const char* value()
  {
    return "#	@section COPYRIGHT\n"
"#	Copyright (C) 2023 Consequential Robotics Ltd\n"
"#	\n"
"#	@section AUTHOR\n"
"#	Consequential Robotics http://consequentialrobotics.com\n"
"#	\n"
"#	@section LICENSE\n"
"#	For a full copy of the license agreement, and a complete\n"
"#	definition of \"The Software\", see LICENSE in the MDK root\n"
"#	directory.\n"
"#	\n"
"#	Subject to the terms of this Agreement, Consequential\n"
"#	Robotics grants to you a limited, non-exclusive, non-\n"
"#	transferable license, without right to sub-license, to use\n"
"#	\"The Software\" in accordance with this Agreement and any\n"
"#	other written agreement with Consequential Robotics.\n"
"#	Consequential Robotics does not transfer the title of \"The\n"
"#	Software\" to you; the license granted to you is not a sale.\n"
"#	This agreement is a binding legal agreement between\n"
"#	Consequential Robotics and the purchasers or users of \"The\n"
"#	Software\".\n"
"#	\n"
"#	THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY\n"
"#	KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE\n"
"#	WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR\n"
"#	PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS\n"
"#	OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR\n"
"#	OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR\n"
"#	OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE\n"
"#	SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n"
"#	\n"
"#\n"
"#	This message defines all of the required parameters needed to annotate\n"
"# the camera images with output from the vision.py library. This is mainly\n"
"# used to provide output to mirocode.\n"
"\n"
"\n"
"\n"
"#### HEADER\n"
"\n"
"# standard header\n"
"std_msgs/Header header\n"
"\n"
"\n"
"\n"
"#### CONTENT\n"
"\n"
"std_msgs/String type\n"
"std_msgs/String cam\n"
"std_msgs/Float32MultiArray centre\n"
"std_msgs/Float32MultiArray vertices\n"
"std_msgs/Float32 size\n"
"std_msgs/Float32 area\n"
"std_msgs/UInt8 id\n"
"std_msgs/Float32 distance\n"
"\n"
"================================================================================\n"
"MSG: std_msgs/Header\n"
"# Standard metadata for higher-level stamped data types.\n"
"# This is generally used to communicate timestamped data \n"
"# in a particular coordinate frame.\n"
"# \n"
"# sequence ID: consecutively increasing ID \n"
"uint32 seq\n"
"#Two-integer timestamp that is expressed as:\n"
"# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n"
"# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n"
"# time-handling sugar is provided by the client library\n"
"time stamp\n"
"#Frame this data is associated with\n"
"string frame_id\n"
"\n"
"================================================================================\n"
"MSG: std_msgs/String\n"
"string data\n"
"\n"
"================================================================================\n"
"MSG: std_msgs/Float32MultiArray\n"
"# Please look at the MultiArrayLayout message definition for\n"
"# documentation on all multiarrays.\n"
"\n"
"MultiArrayLayout  layout        # specification of data layout\n"
"float32[]         data          # array of data\n"
"\n"
"\n"
"================================================================================\n"
"MSG: std_msgs/MultiArrayLayout\n"
"# The multiarray declares a generic multi-dimensional array of a\n"
"# particular data type.  Dimensions are ordered from outer most\n"
"# to inner most.\n"
"\n"
"MultiArrayDimension[] dim # Array of dimension properties\n"
"uint32 data_offset        # padding elements at front of data\n"
"\n"
"# Accessors should ALWAYS be written in terms of dimension stride\n"
"# and specified outer-most dimension first.\n"
"# \n"
"# multiarray(i,j,k) = data[data_offset + dim_stride[1]*i + dim_stride[2]*j + k]\n"
"#\n"
"# A standard, 3-channel 640x480 image with interleaved color channels\n"
"# would be specified as:\n"
"#\n"
"# dim[0].label  = \"height\"\n"
"# dim[0].size   = 480\n"
"# dim[0].stride = 3*640*480 = 921600  (note dim[0] stride is just size of image)\n"
"# dim[1].label  = \"width\"\n"
"# dim[1].size   = 640\n"
"# dim[1].stride = 3*640 = 1920\n"
"# dim[2].label  = \"channel\"\n"
"# dim[2].size   = 3\n"
"# dim[2].stride = 3\n"
"#\n"
"# multiarray(i,j,k) refers to the ith row, jth column, and kth channel.\n"
"\n"
"================================================================================\n"
"MSG: std_msgs/MultiArrayDimension\n"
"string label   # label of given dimension\n"
"uint32 size    # size of given dimension (in type units)\n"
"uint32 stride  # stride of given dimension\n"
"================================================================================\n"
"MSG: std_msgs/Float32\n"
"float32 data\n"
"================================================================================\n"
"MSG: std_msgs/UInt8\n"
"uint8 data\n"
;
  }

  static const char* value(const ::miro2_msg::img_annotation_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::miro2_msg::img_annotation_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.type);
      stream.next(m.cam);
      stream.next(m.centre);
      stream.next(m.vertices);
      stream.next(m.size);
      stream.next(m.area);
      stream.next(m.id);
      stream.next(m.distance);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct img_annotation_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::miro2_msg::img_annotation_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::miro2_msg::img_annotation_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "type: ";
    s << std::endl;
    Printer< ::std_msgs::String_<ContainerAllocator> >::stream(s, indent + "  ", v.type);
    s << indent << "cam: ";
    s << std::endl;
    Printer< ::std_msgs::String_<ContainerAllocator> >::stream(s, indent + "  ", v.cam);
    s << indent << "centre: ";
    s << std::endl;
    Printer< ::std_msgs::Float32MultiArray_<ContainerAllocator> >::stream(s, indent + "  ", v.centre);
    s << indent << "vertices: ";
    s << std::endl;
    Printer< ::std_msgs::Float32MultiArray_<ContainerAllocator> >::stream(s, indent + "  ", v.vertices);
    s << indent << "size: ";
    s << std::endl;
    Printer< ::std_msgs::Float32_<ContainerAllocator> >::stream(s, indent + "  ", v.size);
    s << indent << "area: ";
    s << std::endl;
    Printer< ::std_msgs::Float32_<ContainerAllocator> >::stream(s, indent + "  ", v.area);
    s << indent << "id: ";
    s << std::endl;
    Printer< ::std_msgs::UInt8_<ContainerAllocator> >::stream(s, indent + "  ", v.id);
    s << indent << "distance: ";
    s << std::endl;
    Printer< ::std_msgs::Float32_<ContainerAllocator> >::stream(s, indent + "  ", v.distance);
  }
};

} // namespace message_operations
} // namespace ros

#endif // MIRO2_MSG_MESSAGE_IMG_ANNOTATION_H
