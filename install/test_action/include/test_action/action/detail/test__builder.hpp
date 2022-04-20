// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from test_action:action/Test.idl
// generated code does not contain a copyright notice

#ifndef TEST_ACTION__ACTION__DETAIL__TEST__BUILDER_HPP_
#define TEST_ACTION__ACTION__DETAIL__TEST__BUILDER_HPP_

#include "test_action/action/detail/test__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace test_action
{

namespace action
{

namespace builder
{

class Init_Test_Goal_pose
{
public:
  Init_Test_Goal_pose()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::test_action::action::Test_Goal pose(::test_action::action::Test_Goal::_pose_type arg)
  {
    msg_.pose = std::move(arg);
    return std::move(msg_);
  }

private:
  ::test_action::action::Test_Goal msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::test_action::action::Test_Goal>()
{
  return test_action::action::builder::Init_Test_Goal_pose();
}

}  // namespace test_action


namespace test_action
{

namespace action
{

namespace builder
{

class Init_Test_Result_status
{
public:
  Init_Test_Result_status()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::test_action::action::Test_Result status(::test_action::action::Test_Result::_status_type arg)
  {
    msg_.status = std::move(arg);
    return std::move(msg_);
  }

private:
  ::test_action::action::Test_Result msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::test_action::action::Test_Result>()
{
  return test_action::action::builder::Init_Test_Result_status();
}

}  // namespace test_action


namespace test_action
{

namespace action
{

namespace builder
{

class Init_Test_Feedback_feedback
{
public:
  Init_Test_Feedback_feedback()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::test_action::action::Test_Feedback feedback(::test_action::action::Test_Feedback::_feedback_type arg)
  {
    msg_.feedback = std::move(arg);
    return std::move(msg_);
  }

private:
  ::test_action::action::Test_Feedback msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::test_action::action::Test_Feedback>()
{
  return test_action::action::builder::Init_Test_Feedback_feedback();
}

}  // namespace test_action


namespace test_action
{

namespace action
{

namespace builder
{

class Init_Test_SendGoal_Request_goal
{
public:
  explicit Init_Test_SendGoal_Request_goal(::test_action::action::Test_SendGoal_Request & msg)
  : msg_(msg)
  {}
  ::test_action::action::Test_SendGoal_Request goal(::test_action::action::Test_SendGoal_Request::_goal_type arg)
  {
    msg_.goal = std::move(arg);
    return std::move(msg_);
  }

private:
  ::test_action::action::Test_SendGoal_Request msg_;
};

class Init_Test_SendGoal_Request_goal_id
{
public:
  Init_Test_SendGoal_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Test_SendGoal_Request_goal goal_id(::test_action::action::Test_SendGoal_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_Test_SendGoal_Request_goal(msg_);
  }

private:
  ::test_action::action::Test_SendGoal_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::test_action::action::Test_SendGoal_Request>()
{
  return test_action::action::builder::Init_Test_SendGoal_Request_goal_id();
}

}  // namespace test_action


namespace test_action
{

namespace action
{

namespace builder
{

class Init_Test_SendGoal_Response_stamp
{
public:
  explicit Init_Test_SendGoal_Response_stamp(::test_action::action::Test_SendGoal_Response & msg)
  : msg_(msg)
  {}
  ::test_action::action::Test_SendGoal_Response stamp(::test_action::action::Test_SendGoal_Response::_stamp_type arg)
  {
    msg_.stamp = std::move(arg);
    return std::move(msg_);
  }

private:
  ::test_action::action::Test_SendGoal_Response msg_;
};

class Init_Test_SendGoal_Response_accepted
{
public:
  Init_Test_SendGoal_Response_accepted()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Test_SendGoal_Response_stamp accepted(::test_action::action::Test_SendGoal_Response::_accepted_type arg)
  {
    msg_.accepted = std::move(arg);
    return Init_Test_SendGoal_Response_stamp(msg_);
  }

private:
  ::test_action::action::Test_SendGoal_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::test_action::action::Test_SendGoal_Response>()
{
  return test_action::action::builder::Init_Test_SendGoal_Response_accepted();
}

}  // namespace test_action


namespace test_action
{

namespace action
{

namespace builder
{

class Init_Test_GetResult_Request_goal_id
{
public:
  Init_Test_GetResult_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::test_action::action::Test_GetResult_Request goal_id(::test_action::action::Test_GetResult_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::test_action::action::Test_GetResult_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::test_action::action::Test_GetResult_Request>()
{
  return test_action::action::builder::Init_Test_GetResult_Request_goal_id();
}

}  // namespace test_action


namespace test_action
{

namespace action
{

namespace builder
{

class Init_Test_GetResult_Response_result
{
public:
  explicit Init_Test_GetResult_Response_result(::test_action::action::Test_GetResult_Response & msg)
  : msg_(msg)
  {}
  ::test_action::action::Test_GetResult_Response result(::test_action::action::Test_GetResult_Response::_result_type arg)
  {
    msg_.result = std::move(arg);
    return std::move(msg_);
  }

private:
  ::test_action::action::Test_GetResult_Response msg_;
};

class Init_Test_GetResult_Response_status
{
public:
  Init_Test_GetResult_Response_status()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Test_GetResult_Response_result status(::test_action::action::Test_GetResult_Response::_status_type arg)
  {
    msg_.status = std::move(arg);
    return Init_Test_GetResult_Response_result(msg_);
  }

private:
  ::test_action::action::Test_GetResult_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::test_action::action::Test_GetResult_Response>()
{
  return test_action::action::builder::Init_Test_GetResult_Response_status();
}

}  // namespace test_action


namespace test_action
{

namespace action
{

namespace builder
{

class Init_Test_FeedbackMessage_feedback
{
public:
  explicit Init_Test_FeedbackMessage_feedback(::test_action::action::Test_FeedbackMessage & msg)
  : msg_(msg)
  {}
  ::test_action::action::Test_FeedbackMessage feedback(::test_action::action::Test_FeedbackMessage::_feedback_type arg)
  {
    msg_.feedback = std::move(arg);
    return std::move(msg_);
  }

private:
  ::test_action::action::Test_FeedbackMessage msg_;
};

class Init_Test_FeedbackMessage_goal_id
{
public:
  Init_Test_FeedbackMessage_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Test_FeedbackMessage_feedback goal_id(::test_action::action::Test_FeedbackMessage::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_Test_FeedbackMessage_feedback(msg_);
  }

private:
  ::test_action::action::Test_FeedbackMessage msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::test_action::action::Test_FeedbackMessage>()
{
  return test_action::action::builder::Init_Test_FeedbackMessage_goal_id();
}

}  // namespace test_action

#endif  // TEST_ACTION__ACTION__DETAIL__TEST__BUILDER_HPP_
