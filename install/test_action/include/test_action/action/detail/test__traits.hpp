// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from test_action:action/Test.idl
// generated code does not contain a copyright notice

#ifndef TEST_ACTION__ACTION__DETAIL__TEST__TRAITS_HPP_
#define TEST_ACTION__ACTION__DETAIL__TEST__TRAITS_HPP_

#include "test_action/action/detail/test__struct.hpp"
#include <stdint.h>
#include <rosidl_runtime_cpp/traits.hpp>
#include <sstream>
#include <string>
#include <type_traits>

namespace rosidl_generator_traits
{

inline void to_yaml(
  const test_action::action::Test_Goal & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: pose
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.pose.size() == 0) {
      out << "pose: []\n";
    } else {
      out << "pose:\n";
      for (auto item : msg.pose) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        value_to_yaml(item, out);
        out << "\n";
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const test_action::action::Test_Goal & msg)
{
  std::ostringstream out;
  to_yaml(msg, out);
  return out.str();
}

template<>
inline const char * data_type<test_action::action::Test_Goal>()
{
  return "test_action::action::Test_Goal";
}

template<>
inline const char * name<test_action::action::Test_Goal>()
{
  return "test_action/action/Test_Goal";
}

template<>
struct has_fixed_size<test_action::action::Test_Goal>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<test_action::action::Test_Goal>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<test_action::action::Test_Goal>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

inline void to_yaml(
  const test_action::action::Test_Result & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: status
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "status: ";
    value_to_yaml(msg.status, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const test_action::action::Test_Result & msg)
{
  std::ostringstream out;
  to_yaml(msg, out);
  return out.str();
}

template<>
inline const char * data_type<test_action::action::Test_Result>()
{
  return "test_action::action::Test_Result";
}

template<>
inline const char * name<test_action::action::Test_Result>()
{
  return "test_action/action/Test_Result";
}

template<>
struct has_fixed_size<test_action::action::Test_Result>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<test_action::action::Test_Result>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<test_action::action::Test_Result>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

inline void to_yaml(
  const test_action::action::Test_Feedback & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: feedback
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "feedback: ";
    value_to_yaml(msg.feedback, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const test_action::action::Test_Feedback & msg)
{
  std::ostringstream out;
  to_yaml(msg, out);
  return out.str();
}

template<>
inline const char * data_type<test_action::action::Test_Feedback>()
{
  return "test_action::action::Test_Feedback";
}

template<>
inline const char * name<test_action::action::Test_Feedback>()
{
  return "test_action/action/Test_Feedback";
}

template<>
struct has_fixed_size<test_action::action::Test_Feedback>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<test_action::action::Test_Feedback>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<test_action::action::Test_Feedback>
  : std::true_type {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'goal_id'
#include "unique_identifier_msgs/msg/detail/uuid__traits.hpp"
// Member 'goal'
#include "test_action/action/detail/test__traits.hpp"

namespace rosidl_generator_traits
{

inline void to_yaml(
  const test_action::action::Test_SendGoal_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: goal_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "goal_id:\n";
    to_yaml(msg.goal_id, out, indentation + 2);
  }

  // member: goal
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "goal:\n";
    to_yaml(msg.goal, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const test_action::action::Test_SendGoal_Request & msg)
{
  std::ostringstream out;
  to_yaml(msg, out);
  return out.str();
}

template<>
inline const char * data_type<test_action::action::Test_SendGoal_Request>()
{
  return "test_action::action::Test_SendGoal_Request";
}

template<>
inline const char * name<test_action::action::Test_SendGoal_Request>()
{
  return "test_action/action/Test_SendGoal_Request";
}

template<>
struct has_fixed_size<test_action::action::Test_SendGoal_Request>
  : std::integral_constant<bool, has_fixed_size<test_action::action::Test_Goal>::value && has_fixed_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct has_bounded_size<test_action::action::Test_SendGoal_Request>
  : std::integral_constant<bool, has_bounded_size<test_action::action::Test_Goal>::value && has_bounded_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct is_message<test_action::action::Test_SendGoal_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__traits.hpp"

namespace rosidl_generator_traits
{

inline void to_yaml(
  const test_action::action::Test_SendGoal_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: accepted
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "accepted: ";
    value_to_yaml(msg.accepted, out);
    out << "\n";
  }

  // member: stamp
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "stamp:\n";
    to_yaml(msg.stamp, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const test_action::action::Test_SendGoal_Response & msg)
{
  std::ostringstream out;
  to_yaml(msg, out);
  return out.str();
}

template<>
inline const char * data_type<test_action::action::Test_SendGoal_Response>()
{
  return "test_action::action::Test_SendGoal_Response";
}

template<>
inline const char * name<test_action::action::Test_SendGoal_Response>()
{
  return "test_action/action/Test_SendGoal_Response";
}

template<>
struct has_fixed_size<test_action::action::Test_SendGoal_Response>
  : std::integral_constant<bool, has_fixed_size<builtin_interfaces::msg::Time>::value> {};

template<>
struct has_bounded_size<test_action::action::Test_SendGoal_Response>
  : std::integral_constant<bool, has_bounded_size<builtin_interfaces::msg::Time>::value> {};

template<>
struct is_message<test_action::action::Test_SendGoal_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<test_action::action::Test_SendGoal>()
{
  return "test_action::action::Test_SendGoal";
}

template<>
inline const char * name<test_action::action::Test_SendGoal>()
{
  return "test_action/action/Test_SendGoal";
}

template<>
struct has_fixed_size<test_action::action::Test_SendGoal>
  : std::integral_constant<
    bool,
    has_fixed_size<test_action::action::Test_SendGoal_Request>::value &&
    has_fixed_size<test_action::action::Test_SendGoal_Response>::value
  >
{
};

template<>
struct has_bounded_size<test_action::action::Test_SendGoal>
  : std::integral_constant<
    bool,
    has_bounded_size<test_action::action::Test_SendGoal_Request>::value &&
    has_bounded_size<test_action::action::Test_SendGoal_Response>::value
  >
{
};

template<>
struct is_service<test_action::action::Test_SendGoal>
  : std::true_type
{
};

template<>
struct is_service_request<test_action::action::Test_SendGoal_Request>
  : std::true_type
{
};

template<>
struct is_service_response<test_action::action::Test_SendGoal_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__traits.hpp"

namespace rosidl_generator_traits
{

inline void to_yaml(
  const test_action::action::Test_GetResult_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: goal_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "goal_id:\n";
    to_yaml(msg.goal_id, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const test_action::action::Test_GetResult_Request & msg)
{
  std::ostringstream out;
  to_yaml(msg, out);
  return out.str();
}

template<>
inline const char * data_type<test_action::action::Test_GetResult_Request>()
{
  return "test_action::action::Test_GetResult_Request";
}

template<>
inline const char * name<test_action::action::Test_GetResult_Request>()
{
  return "test_action/action/Test_GetResult_Request";
}

template<>
struct has_fixed_size<test_action::action::Test_GetResult_Request>
  : std::integral_constant<bool, has_fixed_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct has_bounded_size<test_action::action::Test_GetResult_Request>
  : std::integral_constant<bool, has_bounded_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct is_message<test_action::action::Test_GetResult_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'result'
// already included above
// #include "test_action/action/detail/test__traits.hpp"

namespace rosidl_generator_traits
{

inline void to_yaml(
  const test_action::action::Test_GetResult_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: status
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "status: ";
    value_to_yaml(msg.status, out);
    out << "\n";
  }

  // member: result
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "result:\n";
    to_yaml(msg.result, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const test_action::action::Test_GetResult_Response & msg)
{
  std::ostringstream out;
  to_yaml(msg, out);
  return out.str();
}

template<>
inline const char * data_type<test_action::action::Test_GetResult_Response>()
{
  return "test_action::action::Test_GetResult_Response";
}

template<>
inline const char * name<test_action::action::Test_GetResult_Response>()
{
  return "test_action/action/Test_GetResult_Response";
}

template<>
struct has_fixed_size<test_action::action::Test_GetResult_Response>
  : std::integral_constant<bool, has_fixed_size<test_action::action::Test_Result>::value> {};

template<>
struct has_bounded_size<test_action::action::Test_GetResult_Response>
  : std::integral_constant<bool, has_bounded_size<test_action::action::Test_Result>::value> {};

template<>
struct is_message<test_action::action::Test_GetResult_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<test_action::action::Test_GetResult>()
{
  return "test_action::action::Test_GetResult";
}

template<>
inline const char * name<test_action::action::Test_GetResult>()
{
  return "test_action/action/Test_GetResult";
}

template<>
struct has_fixed_size<test_action::action::Test_GetResult>
  : std::integral_constant<
    bool,
    has_fixed_size<test_action::action::Test_GetResult_Request>::value &&
    has_fixed_size<test_action::action::Test_GetResult_Response>::value
  >
{
};

template<>
struct has_bounded_size<test_action::action::Test_GetResult>
  : std::integral_constant<
    bool,
    has_bounded_size<test_action::action::Test_GetResult_Request>::value &&
    has_bounded_size<test_action::action::Test_GetResult_Response>::value
  >
{
};

template<>
struct is_service<test_action::action::Test_GetResult>
  : std::true_type
{
};

template<>
struct is_service_request<test_action::action::Test_GetResult_Request>
  : std::true_type
{
};

template<>
struct is_service_response<test_action::action::Test_GetResult_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__traits.hpp"
// Member 'feedback'
// already included above
// #include "test_action/action/detail/test__traits.hpp"

namespace rosidl_generator_traits
{

inline void to_yaml(
  const test_action::action::Test_FeedbackMessage & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: goal_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "goal_id:\n";
    to_yaml(msg.goal_id, out, indentation + 2);
  }

  // member: feedback
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "feedback:\n";
    to_yaml(msg.feedback, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const test_action::action::Test_FeedbackMessage & msg)
{
  std::ostringstream out;
  to_yaml(msg, out);
  return out.str();
}

template<>
inline const char * data_type<test_action::action::Test_FeedbackMessage>()
{
  return "test_action::action::Test_FeedbackMessage";
}

template<>
inline const char * name<test_action::action::Test_FeedbackMessage>()
{
  return "test_action/action/Test_FeedbackMessage";
}

template<>
struct has_fixed_size<test_action::action::Test_FeedbackMessage>
  : std::integral_constant<bool, has_fixed_size<test_action::action::Test_Feedback>::value && has_fixed_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct has_bounded_size<test_action::action::Test_FeedbackMessage>
  : std::integral_constant<bool, has_bounded_size<test_action::action::Test_Feedback>::value && has_bounded_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct is_message<test_action::action::Test_FeedbackMessage>
  : std::true_type {};

}  // namespace rosidl_generator_traits


namespace rosidl_generator_traits
{

template<>
struct is_action<test_action::action::Test>
  : std::true_type
{
};

template<>
struct is_action_goal<test_action::action::Test_Goal>
  : std::true_type
{
};

template<>
struct is_action_result<test_action::action::Test_Result>
  : std::true_type
{
};

template<>
struct is_action_feedback<test_action::action::Test_Feedback>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits


#endif  // TEST_ACTION__ACTION__DETAIL__TEST__TRAITS_HPP_
