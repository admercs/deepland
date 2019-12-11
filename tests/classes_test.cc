#include <gtest/gtest.h>

#include "classes.h"

namespace {

class ClassesFixture : public ::testing::Test {
 protected:
  First f{5};
  Second s{10};

  // Test constructor
  ClassesFixture() { s.set_id(1); }
  // virtual ~TestFixture();          // Test destructor
  // static void SetUpTestCase();     // Execute before a test
  // static void TearDownTestCase();  // Execute after a test
  // virtual void SetUp();            // Execute globally before all tests
  // virtual void TearDown();         // Execute globally after all tests
};

// Tests factorial of negative numbers.
TEST_F(ClassesFixture, Initialization) {
  // This test is named "Negative", and belongs to the "AdditionSubtraction"
  // test case.

  EXPECT_EQ(f.get_number(), 5);
  EXPECT_EQ(s.get_id(), 1);
  EXPECT_EQ(s.obj.get_number(), 10);

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
}  // namespace
