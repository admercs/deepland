#ifndef CLASSES_H
#define CLASSES_H

#include <string>
#include <vector>

using int_vector = std::vector<int>;

/*! First class for demonstration purposes
    \param name a string
    \param number a double-precision floating-point number
    \param int_vector a vector of integers
*/
class First {
 public:
  std::string name;                  // string
  double number;                     // double-precision floating-point
  int_vector list;                   // vector of int
  First(const double &number);       // constructor
  ~First(){};                        // destructor
  const double &get_number() const;  // getter method
};

/*! Second class for demonstration purposes
    \param obj an object of class First
    \param _id an integer
*/
class Second {
 public:
  First obj;                         // nested class
  Second(const double &number);      // constructor
  ~Second(){};                       // destructor
  void set_id(int value);            // setter method
  const int &get_id() const;         // getter method
  const double &get_number() const;  // getter method

 private:
  int _id;  // private int
};

#endif
