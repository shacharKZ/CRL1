// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from test_action:action/Test.idl
// generated code does not contain a copyright notice
#include "test_action/action/detail/test__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// Include directives for member types
// Member `pose`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

bool
test_action__action__Test_Goal__init(test_action__action__Test_Goal * msg)
{
  if (!msg) {
    return false;
  }
  // pose
  if (!rosidl_runtime_c__float__Sequence__init(&msg->pose, 0)) {
    test_action__action__Test_Goal__fini(msg);
    return false;
  }
  return true;
}

void
test_action__action__Test_Goal__fini(test_action__action__Test_Goal * msg)
{
  if (!msg) {
    return;
  }
  // pose
  rosidl_runtime_c__float__Sequence__fini(&msg->pose);
}

test_action__action__Test_Goal *
test_action__action__Test_Goal__create()
{
  test_action__action__Test_Goal * msg = (test_action__action__Test_Goal *)malloc(sizeof(test_action__action__Test_Goal));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(test_action__action__Test_Goal));
  bool success = test_action__action__Test_Goal__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
test_action__action__Test_Goal__destroy(test_action__action__Test_Goal * msg)
{
  if (msg) {
    test_action__action__Test_Goal__fini(msg);
  }
  free(msg);
}


bool
test_action__action__Test_Goal__Sequence__init(test_action__action__Test_Goal__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  test_action__action__Test_Goal * data = NULL;
  if (size) {
    data = (test_action__action__Test_Goal *)calloc(size, sizeof(test_action__action__Test_Goal));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = test_action__action__Test_Goal__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        test_action__action__Test_Goal__fini(&data[i - 1]);
      }
      free(data);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
test_action__action__Test_Goal__Sequence__fini(test_action__action__Test_Goal__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      test_action__action__Test_Goal__fini(&array->data[i]);
    }
    free(array->data);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

test_action__action__Test_Goal__Sequence *
test_action__action__Test_Goal__Sequence__create(size_t size)
{
  test_action__action__Test_Goal__Sequence * array = (test_action__action__Test_Goal__Sequence *)malloc(sizeof(test_action__action__Test_Goal__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = test_action__action__Test_Goal__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
test_action__action__Test_Goal__Sequence__destroy(test_action__action__Test_Goal__Sequence * array)
{
  if (array) {
    test_action__action__Test_Goal__Sequence__fini(array);
  }
  free(array);
}


// Include directives for member types
// Member `status`
#include "rosidl_runtime_c/string_functions.h"

bool
test_action__action__Test_Result__init(test_action__action__Test_Result * msg)
{
  if (!msg) {
    return false;
  }
  // status
  if (!rosidl_runtime_c__String__init(&msg->status)) {
    test_action__action__Test_Result__fini(msg);
    return false;
  }
  return true;
}

void
test_action__action__Test_Result__fini(test_action__action__Test_Result * msg)
{
  if (!msg) {
    return;
  }
  // status
  rosidl_runtime_c__String__fini(&msg->status);
}

test_action__action__Test_Result *
test_action__action__Test_Result__create()
{
  test_action__action__Test_Result * msg = (test_action__action__Test_Result *)malloc(sizeof(test_action__action__Test_Result));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(test_action__action__Test_Result));
  bool success = test_action__action__Test_Result__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
test_action__action__Test_Result__destroy(test_action__action__Test_Result * msg)
{
  if (msg) {
    test_action__action__Test_Result__fini(msg);
  }
  free(msg);
}


bool
test_action__action__Test_Result__Sequence__init(test_action__action__Test_Result__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  test_action__action__Test_Result * data = NULL;
  if (size) {
    data = (test_action__action__Test_Result *)calloc(size, sizeof(test_action__action__Test_Result));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = test_action__action__Test_Result__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        test_action__action__Test_Result__fini(&data[i - 1]);
      }
      free(data);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
test_action__action__Test_Result__Sequence__fini(test_action__action__Test_Result__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      test_action__action__Test_Result__fini(&array->data[i]);
    }
    free(array->data);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

test_action__action__Test_Result__Sequence *
test_action__action__Test_Result__Sequence__create(size_t size)
{
  test_action__action__Test_Result__Sequence * array = (test_action__action__Test_Result__Sequence *)malloc(sizeof(test_action__action__Test_Result__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = test_action__action__Test_Result__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
test_action__action__Test_Result__Sequence__destroy(test_action__action__Test_Result__Sequence * array)
{
  if (array) {
    test_action__action__Test_Result__Sequence__fini(array);
  }
  free(array);
}


// Include directives for member types
// Member `feedback`
// already included above
// #include "rosidl_runtime_c/string_functions.h"

bool
test_action__action__Test_Feedback__init(test_action__action__Test_Feedback * msg)
{
  if (!msg) {
    return false;
  }
  // feedback
  if (!rosidl_runtime_c__String__init(&msg->feedback)) {
    test_action__action__Test_Feedback__fini(msg);
    return false;
  }
  return true;
}

void
test_action__action__Test_Feedback__fini(test_action__action__Test_Feedback * msg)
{
  if (!msg) {
    return;
  }
  // feedback
  rosidl_runtime_c__String__fini(&msg->feedback);
}

test_action__action__Test_Feedback *
test_action__action__Test_Feedback__create()
{
  test_action__action__Test_Feedback * msg = (test_action__action__Test_Feedback *)malloc(sizeof(test_action__action__Test_Feedback));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(test_action__action__Test_Feedback));
  bool success = test_action__action__Test_Feedback__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
test_action__action__Test_Feedback__destroy(test_action__action__Test_Feedback * msg)
{
  if (msg) {
    test_action__action__Test_Feedback__fini(msg);
  }
  free(msg);
}


bool
test_action__action__Test_Feedback__Sequence__init(test_action__action__Test_Feedback__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  test_action__action__Test_Feedback * data = NULL;
  if (size) {
    data = (test_action__action__Test_Feedback *)calloc(size, sizeof(test_action__action__Test_Feedback));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = test_action__action__Test_Feedback__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        test_action__action__Test_Feedback__fini(&data[i - 1]);
      }
      free(data);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
test_action__action__Test_Feedback__Sequence__fini(test_action__action__Test_Feedback__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      test_action__action__Test_Feedback__fini(&array->data[i]);
    }
    free(array->data);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

test_action__action__Test_Feedback__Sequence *
test_action__action__Test_Feedback__Sequence__create(size_t size)
{
  test_action__action__Test_Feedback__Sequence * array = (test_action__action__Test_Feedback__Sequence *)malloc(sizeof(test_action__action__Test_Feedback__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = test_action__action__Test_Feedback__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
test_action__action__Test_Feedback__Sequence__destroy(test_action__action__Test_Feedback__Sequence * array)
{
  if (array) {
    test_action__action__Test_Feedback__Sequence__fini(array);
  }
  free(array);
}


// Include directives for member types
// Member `goal_id`
#include "unique_identifier_msgs/msg/detail/uuid__functions.h"
// Member `goal`
// already included above
// #include "test_action/action/detail/test__functions.h"

bool
test_action__action__Test_SendGoal_Request__init(test_action__action__Test_SendGoal_Request * msg)
{
  if (!msg) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__init(&msg->goal_id)) {
    test_action__action__Test_SendGoal_Request__fini(msg);
    return false;
  }
  // goal
  if (!test_action__action__Test_Goal__init(&msg->goal)) {
    test_action__action__Test_SendGoal_Request__fini(msg);
    return false;
  }
  return true;
}

void
test_action__action__Test_SendGoal_Request__fini(test_action__action__Test_SendGoal_Request * msg)
{
  if (!msg) {
    return;
  }
  // goal_id
  unique_identifier_msgs__msg__UUID__fini(&msg->goal_id);
  // goal
  test_action__action__Test_Goal__fini(&msg->goal);
}

test_action__action__Test_SendGoal_Request *
test_action__action__Test_SendGoal_Request__create()
{
  test_action__action__Test_SendGoal_Request * msg = (test_action__action__Test_SendGoal_Request *)malloc(sizeof(test_action__action__Test_SendGoal_Request));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(test_action__action__Test_SendGoal_Request));
  bool success = test_action__action__Test_SendGoal_Request__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
test_action__action__Test_SendGoal_Request__destroy(test_action__action__Test_SendGoal_Request * msg)
{
  if (msg) {
    test_action__action__Test_SendGoal_Request__fini(msg);
  }
  free(msg);
}


bool
test_action__action__Test_SendGoal_Request__Sequence__init(test_action__action__Test_SendGoal_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  test_action__action__Test_SendGoal_Request * data = NULL;
  if (size) {
    data = (test_action__action__Test_SendGoal_Request *)calloc(size, sizeof(test_action__action__Test_SendGoal_Request));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = test_action__action__Test_SendGoal_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        test_action__action__Test_SendGoal_Request__fini(&data[i - 1]);
      }
      free(data);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
test_action__action__Test_SendGoal_Request__Sequence__fini(test_action__action__Test_SendGoal_Request__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      test_action__action__Test_SendGoal_Request__fini(&array->data[i]);
    }
    free(array->data);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

test_action__action__Test_SendGoal_Request__Sequence *
test_action__action__Test_SendGoal_Request__Sequence__create(size_t size)
{
  test_action__action__Test_SendGoal_Request__Sequence * array = (test_action__action__Test_SendGoal_Request__Sequence *)malloc(sizeof(test_action__action__Test_SendGoal_Request__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = test_action__action__Test_SendGoal_Request__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
test_action__action__Test_SendGoal_Request__Sequence__destroy(test_action__action__Test_SendGoal_Request__Sequence * array)
{
  if (array) {
    test_action__action__Test_SendGoal_Request__Sequence__fini(array);
  }
  free(array);
}


// Include directives for member types
// Member `stamp`
#include "builtin_interfaces/msg/detail/time__functions.h"

bool
test_action__action__Test_SendGoal_Response__init(test_action__action__Test_SendGoal_Response * msg)
{
  if (!msg) {
    return false;
  }
  // accepted
  // stamp
  if (!builtin_interfaces__msg__Time__init(&msg->stamp)) {
    test_action__action__Test_SendGoal_Response__fini(msg);
    return false;
  }
  return true;
}

void
test_action__action__Test_SendGoal_Response__fini(test_action__action__Test_SendGoal_Response * msg)
{
  if (!msg) {
    return;
  }
  // accepted
  // stamp
  builtin_interfaces__msg__Time__fini(&msg->stamp);
}

test_action__action__Test_SendGoal_Response *
test_action__action__Test_SendGoal_Response__create()
{
  test_action__action__Test_SendGoal_Response * msg = (test_action__action__Test_SendGoal_Response *)malloc(sizeof(test_action__action__Test_SendGoal_Response));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(test_action__action__Test_SendGoal_Response));
  bool success = test_action__action__Test_SendGoal_Response__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
test_action__action__Test_SendGoal_Response__destroy(test_action__action__Test_SendGoal_Response * msg)
{
  if (msg) {
    test_action__action__Test_SendGoal_Response__fini(msg);
  }
  free(msg);
}


bool
test_action__action__Test_SendGoal_Response__Sequence__init(test_action__action__Test_SendGoal_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  test_action__action__Test_SendGoal_Response * data = NULL;
  if (size) {
    data = (test_action__action__Test_SendGoal_Response *)calloc(size, sizeof(test_action__action__Test_SendGoal_Response));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = test_action__action__Test_SendGoal_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        test_action__action__Test_SendGoal_Response__fini(&data[i - 1]);
      }
      free(data);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
test_action__action__Test_SendGoal_Response__Sequence__fini(test_action__action__Test_SendGoal_Response__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      test_action__action__Test_SendGoal_Response__fini(&array->data[i]);
    }
    free(array->data);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

test_action__action__Test_SendGoal_Response__Sequence *
test_action__action__Test_SendGoal_Response__Sequence__create(size_t size)
{
  test_action__action__Test_SendGoal_Response__Sequence * array = (test_action__action__Test_SendGoal_Response__Sequence *)malloc(sizeof(test_action__action__Test_SendGoal_Response__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = test_action__action__Test_SendGoal_Response__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
test_action__action__Test_SendGoal_Response__Sequence__destroy(test_action__action__Test_SendGoal_Response__Sequence * array)
{
  if (array) {
    test_action__action__Test_SendGoal_Response__Sequence__fini(array);
  }
  free(array);
}


// Include directives for member types
// Member `goal_id`
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__functions.h"

bool
test_action__action__Test_GetResult_Request__init(test_action__action__Test_GetResult_Request * msg)
{
  if (!msg) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__init(&msg->goal_id)) {
    test_action__action__Test_GetResult_Request__fini(msg);
    return false;
  }
  return true;
}

void
test_action__action__Test_GetResult_Request__fini(test_action__action__Test_GetResult_Request * msg)
{
  if (!msg) {
    return;
  }
  // goal_id
  unique_identifier_msgs__msg__UUID__fini(&msg->goal_id);
}

test_action__action__Test_GetResult_Request *
test_action__action__Test_GetResult_Request__create()
{
  test_action__action__Test_GetResult_Request * msg = (test_action__action__Test_GetResult_Request *)malloc(sizeof(test_action__action__Test_GetResult_Request));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(test_action__action__Test_GetResult_Request));
  bool success = test_action__action__Test_GetResult_Request__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
test_action__action__Test_GetResult_Request__destroy(test_action__action__Test_GetResult_Request * msg)
{
  if (msg) {
    test_action__action__Test_GetResult_Request__fini(msg);
  }
  free(msg);
}


bool
test_action__action__Test_GetResult_Request__Sequence__init(test_action__action__Test_GetResult_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  test_action__action__Test_GetResult_Request * data = NULL;
  if (size) {
    data = (test_action__action__Test_GetResult_Request *)calloc(size, sizeof(test_action__action__Test_GetResult_Request));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = test_action__action__Test_GetResult_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        test_action__action__Test_GetResult_Request__fini(&data[i - 1]);
      }
      free(data);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
test_action__action__Test_GetResult_Request__Sequence__fini(test_action__action__Test_GetResult_Request__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      test_action__action__Test_GetResult_Request__fini(&array->data[i]);
    }
    free(array->data);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

test_action__action__Test_GetResult_Request__Sequence *
test_action__action__Test_GetResult_Request__Sequence__create(size_t size)
{
  test_action__action__Test_GetResult_Request__Sequence * array = (test_action__action__Test_GetResult_Request__Sequence *)malloc(sizeof(test_action__action__Test_GetResult_Request__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = test_action__action__Test_GetResult_Request__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
test_action__action__Test_GetResult_Request__Sequence__destroy(test_action__action__Test_GetResult_Request__Sequence * array)
{
  if (array) {
    test_action__action__Test_GetResult_Request__Sequence__fini(array);
  }
  free(array);
}


// Include directives for member types
// Member `result`
// already included above
// #include "test_action/action/detail/test__functions.h"

bool
test_action__action__Test_GetResult_Response__init(test_action__action__Test_GetResult_Response * msg)
{
  if (!msg) {
    return false;
  }
  // status
  // result
  if (!test_action__action__Test_Result__init(&msg->result)) {
    test_action__action__Test_GetResult_Response__fini(msg);
    return false;
  }
  return true;
}

void
test_action__action__Test_GetResult_Response__fini(test_action__action__Test_GetResult_Response * msg)
{
  if (!msg) {
    return;
  }
  // status
  // result
  test_action__action__Test_Result__fini(&msg->result);
}

test_action__action__Test_GetResult_Response *
test_action__action__Test_GetResult_Response__create()
{
  test_action__action__Test_GetResult_Response * msg = (test_action__action__Test_GetResult_Response *)malloc(sizeof(test_action__action__Test_GetResult_Response));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(test_action__action__Test_GetResult_Response));
  bool success = test_action__action__Test_GetResult_Response__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
test_action__action__Test_GetResult_Response__destroy(test_action__action__Test_GetResult_Response * msg)
{
  if (msg) {
    test_action__action__Test_GetResult_Response__fini(msg);
  }
  free(msg);
}


bool
test_action__action__Test_GetResult_Response__Sequence__init(test_action__action__Test_GetResult_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  test_action__action__Test_GetResult_Response * data = NULL;
  if (size) {
    data = (test_action__action__Test_GetResult_Response *)calloc(size, sizeof(test_action__action__Test_GetResult_Response));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = test_action__action__Test_GetResult_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        test_action__action__Test_GetResult_Response__fini(&data[i - 1]);
      }
      free(data);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
test_action__action__Test_GetResult_Response__Sequence__fini(test_action__action__Test_GetResult_Response__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      test_action__action__Test_GetResult_Response__fini(&array->data[i]);
    }
    free(array->data);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

test_action__action__Test_GetResult_Response__Sequence *
test_action__action__Test_GetResult_Response__Sequence__create(size_t size)
{
  test_action__action__Test_GetResult_Response__Sequence * array = (test_action__action__Test_GetResult_Response__Sequence *)malloc(sizeof(test_action__action__Test_GetResult_Response__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = test_action__action__Test_GetResult_Response__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
test_action__action__Test_GetResult_Response__Sequence__destroy(test_action__action__Test_GetResult_Response__Sequence * array)
{
  if (array) {
    test_action__action__Test_GetResult_Response__Sequence__fini(array);
  }
  free(array);
}


// Include directives for member types
// Member `goal_id`
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__functions.h"
// Member `feedback`
// already included above
// #include "test_action/action/detail/test__functions.h"

bool
test_action__action__Test_FeedbackMessage__init(test_action__action__Test_FeedbackMessage * msg)
{
  if (!msg) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__init(&msg->goal_id)) {
    test_action__action__Test_FeedbackMessage__fini(msg);
    return false;
  }
  // feedback
  if (!test_action__action__Test_Feedback__init(&msg->feedback)) {
    test_action__action__Test_FeedbackMessage__fini(msg);
    return false;
  }
  return true;
}

void
test_action__action__Test_FeedbackMessage__fini(test_action__action__Test_FeedbackMessage * msg)
{
  if (!msg) {
    return;
  }
  // goal_id
  unique_identifier_msgs__msg__UUID__fini(&msg->goal_id);
  // feedback
  test_action__action__Test_Feedback__fini(&msg->feedback);
}

test_action__action__Test_FeedbackMessage *
test_action__action__Test_FeedbackMessage__create()
{
  test_action__action__Test_FeedbackMessage * msg = (test_action__action__Test_FeedbackMessage *)malloc(sizeof(test_action__action__Test_FeedbackMessage));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(test_action__action__Test_FeedbackMessage));
  bool success = test_action__action__Test_FeedbackMessage__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
test_action__action__Test_FeedbackMessage__destroy(test_action__action__Test_FeedbackMessage * msg)
{
  if (msg) {
    test_action__action__Test_FeedbackMessage__fini(msg);
  }
  free(msg);
}


bool
test_action__action__Test_FeedbackMessage__Sequence__init(test_action__action__Test_FeedbackMessage__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  test_action__action__Test_FeedbackMessage * data = NULL;
  if (size) {
    data = (test_action__action__Test_FeedbackMessage *)calloc(size, sizeof(test_action__action__Test_FeedbackMessage));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = test_action__action__Test_FeedbackMessage__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        test_action__action__Test_FeedbackMessage__fini(&data[i - 1]);
      }
      free(data);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
test_action__action__Test_FeedbackMessage__Sequence__fini(test_action__action__Test_FeedbackMessage__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      test_action__action__Test_FeedbackMessage__fini(&array->data[i]);
    }
    free(array->data);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

test_action__action__Test_FeedbackMessage__Sequence *
test_action__action__Test_FeedbackMessage__Sequence__create(size_t size)
{
  test_action__action__Test_FeedbackMessage__Sequence * array = (test_action__action__Test_FeedbackMessage__Sequence *)malloc(sizeof(test_action__action__Test_FeedbackMessage__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = test_action__action__Test_FeedbackMessage__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
test_action__action__Test_FeedbackMessage__Sequence__destroy(test_action__action__Test_FeedbackMessage__Sequence * array)
{
  if (array) {
    test_action__action__Test_FeedbackMessage__Sequence__fini(array);
  }
  free(array);
}
