// Generated by gencpp from file miro2_msg/priority_peak.msg
// DO NOT EDIT!


#ifndef MIRO2_MSG_MESSAGE_PRIORITY_PEAK_H
#define MIRO2_MSG_MESSAGE_PRIORITY_PEAK_H


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
struct priority_peak_
{
  typedef priority_peak_<ContainerAllocator> Type;

  priority_peak_()
    : stream_index(0)
    , loc_d()
    , height(0.0)
    , size(0.0)
    , azim(0.0)
    , elev(0.0)
    , size_norm(0.0)
    , volume(0.0)
    , range(0.0)
    , actioned(0)  {
      loc_d.assign(0.0);
  }
  priority_peak_(const ContainerAllocator& _alloc)
    : stream_index(0)
    , loc_d()
    , height(0.0)
    , size(0.0)
    , azim(0.0)
    , elev(0.0)
    , size_norm(0.0)
    , volume(0.0)
    , range(0.0)
    , actioned(0)  {
  (void)_alloc;
      loc_d.assign(0.0);
  }



   typedef int32_t _stream_index_type;
  _stream_index_type stream_index;

   typedef boost::array<float, 2>  _loc_d_type;
  _loc_d_type loc_d;

   typedef float _height_type;
  _height_type height;

   typedef float _size_type;
  _size_type size;

   typedef float _azim_type;
  _azim_type azim;

   typedef float _elev_type;
  _elev_type elev;

   typedef float _size_norm_type;
  _size_norm_type size_norm;

   typedef float _volume_type;
  _volume_type volume;

   typedef float _range_type;
  _range_type range;

   typedef int32_t _actioned_type;
  _actioned_type actioned;





  typedef boost::shared_ptr< ::miro2_msg::priority_peak_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::miro2_msg::priority_peak_<ContainerAllocator> const> ConstPtr;

}; // struct priority_peak_

typedef ::miro2_msg::priority_peak_<std::allocator<void> > priority_peak;

typedef boost::shared_ptr< ::miro2_msg::priority_peak > priority_peakPtr;
typedef boost::shared_ptr< ::miro2_msg::priority_peak const> priority_peakConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::miro2_msg::priority_peak_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::miro2_msg::priority_peak_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::miro2_msg::priority_peak_<ContainerAllocator1> & lhs, const ::miro2_msg::priority_peak_<ContainerAllocator2> & rhs)
{
  return lhs.stream_index == rhs.stream_index &&
    lhs.loc_d == rhs.loc_d &&
    lhs.height == rhs.height &&
    lhs.size == rhs.size &&
    lhs.azim == rhs.azim &&
    lhs.elev == rhs.elev &&
    lhs.size_norm == rhs.size_norm &&
    lhs.volume == rhs.volume &&
    lhs.range == rhs.range &&
    lhs.actioned == rhs.actioned;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::miro2_msg::priority_peak_<ContainerAllocator1> & lhs, const ::miro2_msg::priority_peak_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace miro2_msg

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::miro2_msg::priority_peak_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::miro2_msg::priority_peak_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::miro2_msg::priority_peak_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::miro2_msg::priority_peak_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::miro2_msg::priority_peak_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::miro2_msg::priority_peak_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::miro2_msg::priority_peak_<ContainerAllocator> >
{
  static const char* value()
  {
    return "d2924675ffe77da16f66ce7eb1cbeb6d";
  }

  static const char* value(const ::miro2_msg::priority_peak_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xd2924675ffe77da1ULL;
  static const uint64_t static_value2 = 0x6f66ce7eb1cbeb6dULL;
};

template<class ContainerAllocator>
struct DataType< ::miro2_msg::priority_peak_<ContainerAllocator> >
{
  static const char* value()
  {
    return "miro2_msg/priority_peak";
  }

  static const char* value(const ::miro2_msg::priority_peak_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::miro2_msg::priority_peak_<ContainerAllocator> >
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
"\n"
"int32 stream_index\n"
"float32[2] loc_d\n"
"float32 height\n"
"float32 size\n"
"float32 azim\n"
"float32 elev\n"
"\n"
"float32 size_norm\n"
"float32 volume\n"
"float32 range\n"
"\n"
"int32 actioned\n"
"\n"
;
  }

  static const char* value(const ::miro2_msg::priority_peak_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::miro2_msg::priority_peak_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.stream_index);
      stream.next(m.loc_d);
      stream.next(m.height);
      stream.next(m.size);
      stream.next(m.azim);
      stream.next(m.elev);
      stream.next(m.size_norm);
      stream.next(m.volume);
      stream.next(m.range);
      stream.next(m.actioned);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct priority_peak_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::miro2_msg::priority_peak_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::miro2_msg::priority_peak_<ContainerAllocator>& v)
  {
    s << indent << "stream_index: ";
    Printer<int32_t>::stream(s, indent + "  ", v.stream_index);
    s << indent << "loc_d[]" << std::endl;
    for (size_t i = 0; i < v.loc_d.size(); ++i)
    {
      s << indent << "  loc_d[" << i << "]: ";
      Printer<float>::stream(s, indent + "  ", v.loc_d[i]);
    }
    s << indent << "height: ";
    Printer<float>::stream(s, indent + "  ", v.height);
    s << indent << "size: ";
    Printer<float>::stream(s, indent + "  ", v.size);
    s << indent << "azim: ";
    Printer<float>::stream(s, indent + "  ", v.azim);
    s << indent << "elev: ";
    Printer<float>::stream(s, indent + "  ", v.elev);
    s << indent << "size_norm: ";
    Printer<float>::stream(s, indent + "  ", v.size_norm);
    s << indent << "volume: ";
    Printer<float>::stream(s, indent + "  ", v.volume);
    s << indent << "range: ";
    Printer<float>::stream(s, indent + "  ", v.range);
    s << indent << "actioned: ";
    Printer<int32_t>::stream(s, indent + "  ", v.actioned);
  }
};

} // namespace message_operations
} // namespace ros

#endif // MIRO2_MSG_MESSAGE_PRIORITY_PEAK_H
