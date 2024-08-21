// Generated by gencpp from file miro2_msg/adjust.msg
// DO NOT EDIT!


#ifndef MIRO2_MSG_MESSAGE_ADJUST_H
#define MIRO2_MSG_MESSAGE_ADJUST_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace miro2_msg
{
template <class ContainerAllocator>
struct adjust_
{
  typedef adjust_<ContainerAllocator> Type;

  adjust_()
    : data(0.0)
    , gamma(0.0)  {
    }
  adjust_(const ContainerAllocator& _alloc)
    : data(0.0)
    , gamma(0.0)  {
  (void)_alloc;
    }



   typedef float _data_type;
  _data_type data;

   typedef float _gamma_type;
  _gamma_type gamma;





  typedef boost::shared_ptr< ::miro2_msg::adjust_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::miro2_msg::adjust_<ContainerAllocator> const> ConstPtr;

}; // struct adjust_

typedef ::miro2_msg::adjust_<std::allocator<void> > adjust;

typedef boost::shared_ptr< ::miro2_msg::adjust > adjustPtr;
typedef boost::shared_ptr< ::miro2_msg::adjust const> adjustConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::miro2_msg::adjust_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::miro2_msg::adjust_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::miro2_msg::adjust_<ContainerAllocator1> & lhs, const ::miro2_msg::adjust_<ContainerAllocator2> & rhs)
{
  return lhs.data == rhs.data &&
    lhs.gamma == rhs.gamma;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::miro2_msg::adjust_<ContainerAllocator1> & lhs, const ::miro2_msg::adjust_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace miro2_msg

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::miro2_msg::adjust_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::miro2_msg::adjust_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::miro2_msg::adjust_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::miro2_msg::adjust_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::miro2_msg::adjust_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::miro2_msg::adjust_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::miro2_msg::adjust_<ContainerAllocator> >
{
  static const char* value()
  {
    return "f57be85f314b6a6c4ab78af0ca827a06";
  }

  static const char* value(const ::miro2_msg::adjust_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xf57be85f314b6a6cULL;
  static const uint64_t static_value2 = 0x4ab78af0ca827a06ULL;
};

template<class ContainerAllocator>
struct DataType< ::miro2_msg::adjust_<ContainerAllocator> >
{
  static const char* value()
  {
    return "miro2_msg/adjust";
  }

  static const char* value(const ::miro2_msg::adjust_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::miro2_msg::adjust_<ContainerAllocator> >
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
"#	Adjust message provides a route for directly adjusting\n"
"#	a state of the biomimetic model. There are two ways to\n"
"#	specify an adjustment, selected independently for each\n"
"#	adjustment channel.\n"
"#\n"
"#	1) Provide a target value in \"data\" and a \"gamma\" value\n"
"#	between 0 and 1 to cause the state to approach the target:\n"
"#\n"
"#	(at 50Hz)\n"
"#	state += gamma * (data - state)\n"
"#\n"
"#	2) Provide a delta value in \"data\" and set \"gamma\"\n"
"#	to -1 to indicate this drive mode:\n"
"#\n"
"#	(at 50Hz)\n"
"#	state += data\n"
"#\n"
"#	Understood values of gamma, therefore, are:\n"
"#	   -1 : add \"data\" to state\n"
"#	    0 : do nothing\n"
"#	  0-1 : move state towards \"data\"\n"
"#	    1 : instantly set state to \"data\"\n"
"\n"
"float32 data\n"
"float32 gamma\n"
"\n"
;
  }

  static const char* value(const ::miro2_msg::adjust_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::miro2_msg::adjust_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.data);
      stream.next(m.gamma);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct adjust_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::miro2_msg::adjust_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::miro2_msg::adjust_<ContainerAllocator>& v)
  {
    s << indent << "data: ";
    Printer<float>::stream(s, indent + "  ", v.data);
    s << indent << "gamma: ";
    Printer<float>::stream(s, indent + "  ", v.gamma);
  }
};

} // namespace message_operations
} // namespace ros

#endif // MIRO2_MSG_MESSAGE_ADJUST_H
