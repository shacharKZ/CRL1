// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from test_action:action/Test.idl
// generated code does not contain a copyright notice

#ifndef TEST_ACTION__ACTION__DETAIL__TEST__STRUCT_H_
#define TEST_ACTION__ACTION__DETAIL__TEST__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'pose'
#include "rosidl_runtime_c/primitives_sequence.h"

// Struct defined in action/Test in the package test_action.
typedef struct test_action__action__Test_Goal
{
  rosidl_runtime_c__float__Sequence pose;
} test_action__action__Test_Goal;

// Struct for a sequence of test_action__action__Test_Goal.
typedef struct test_action__action__Test_Goal__Sequence
{
  test_action__action__Test_Goal * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} test_action__action__Test_Goal__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'status'
#include "rosidl_runtime_c/string.h"

// Struct defined in action/Test in the package test_action.
typedef struct test_action__action__Test_Result
{
  rosidl_runtime_c__String status;
} test_action__action__Test_Result;

// Struct for a sequence of test_action__action__Test_Result.
typedef struct test_action__action__Test_Result__Sequence
{
  test_action__action__Test_Result * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} test_action__action__Test_Result__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'feedback'
// already included above
// #include "rosidl_runtime_c/string.h"

// Struct defined in action/Test in the package test_action.
typedef struct test_action__action__Test_Feedback
{
  rosidl_runtime_c__String feedback;
} test_action__action__Test_Feedback;

// Struct for a sequence of test_action__action__Test_Feedback.
typedef struct test_action__action__Test_Feedback__Sequence
{
  test_action__action__Test_Feedback * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} test_action__action__Test_Feedback__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
#include "unique_identifier_msgs/msg/detail/uuid__struct.h"
// Member 'goal'
#include "test_action/action/detail/test__struct.h"

// Struct defined in action/Test in the package test_action.
typedef struct test_action__action__Test_SendGoal_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
  test_action__action__Test_Goal goal;
} test_action__action__Test_SendGoal_Request;

// Struct for a sequence of test_action__action__Test_SendGoal_Request.
typedef struct test_action__action__Test_SendGoal_Request__Sequence
{
  test_action__action__Test_SendGoal_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} test_action__action__Test_SendGoal_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__struct.h"

// Struct defined in action/Test in the package test_action.
typedef struct test_action__action__Test_SendGoal_Response
{
  bool accepted;
  builtin_interfaces__msg__Time stamp;
} test_action__action__Test_SendGoal_Response;

// Struct for a sequence of test_action__action__Test_SendGoal_Response.
typedef struct test_action__action__Test_SendGoal_Response__Sequence
{
  test_action__action__Test_SendGoal_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} test_action__action__Test_SendGoal_Response__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.h"

// Struct defined in action/Test in the package test_action.
typedef struct test_action__action__Test_GetResult_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
} test_action__action__Test_GetResult_Request;

// Struct for a sequence of test_action__action__Test_GetResult_Request.
typedef struct test_action__action__Test_GetResult_Request__Sequence
{
  test_action__action__Test_GetResult_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} test_action__action__Test_GetResult_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'result'
// already included above
// #include "test_action/action/detail/test__struct.h"

// Struct defined in action/Test in the package test_action.
typedef struct test_action__action__Test_GetResult_Response
{
  int8_t status;
  test_action__action__Test_Result result;
} test_action__action__Test_GetResult_Response;

// Struct for a sequence of test_action__action__Test_GetResult_Response.
typedef struct test_action__action__Test_GetResult_Response__Sequence
{
  test_action__action__Test_GetResult_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} test_action__action__Test_GetResult_Response__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.h"
// Member 'feedback'
// already included above
// #include "test_action/action/detail/test__struct.h"

// Struct defined in action/Test in the package test_action.
typedef struct test_action__action__Test_FeedbackMessage
{
  unique_identifier_msgs__msg__UUID goal_id;
  test_action__action__Test_Feedback feedback;
} test_action__action__Test_FeedbackMessage;

// Struct for a sequence of test_action__action__Test_FeedbackMessage.
typedef struct test_action__action__Test_FeedbackMessage__Sequence
{
  test_action__action__Test_FeedbackMessage * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} test_action__action__Test_FeedbackMessage__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // TEST_ACTION__ACTION__DETAIL__TEST__STRUCT_H_
