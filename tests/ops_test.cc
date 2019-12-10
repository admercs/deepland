#include <gtest/gtest.h>

#include "ops.h"

namespace {

  // Tests factorial of negative numbers.
  TEST(AdditionSubtraction, Positive) {
    // This test is named "Negative", and belongs to the "AdditionSubtraction"
    // test case.
    EXPECT_EQ(add(1, 1), 2);
    EXPECT_EQ(subtract(1, 1), 0);

    // <TechnicalDetails>
    //
    // EXPECT_EQ(expected, actual) is the same as
    //
    //   EXPECT_TRUE((expected) == (actual))
    //
    // except that it will print both the expected value and the actual
    // value when the assertion fails.  This is very helpful for
    // debugging.  Therefore in this case EXPECT_EQ is preferred.
    //
    // On the other hand, EXPECT_TRUE accepts any Boolean expression,
    // and is thus more general.
    //
    // </TechnicalDetails>
  }
}
