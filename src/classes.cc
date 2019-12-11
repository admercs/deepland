#include "classes.h"

//
// First
//

/*! Constructor
 */
First::First(const double &number) : number(number){};

/*! Get the member number
 */
const double &First::get_number() const { return number; }

//
// Second
//

/*! Constructor; initializes nested First class with argument `number`
 */
Second::Second(const double &number) : obj(number){};

/*! Set the private member id
 */
void Second::set_id(int value) { _id = value; }

/*! Get the private member id
 */
const int &Second::get_id() const { return _id; }

/*! Get the member number
 */
const double &Second::get_number() const { return obj.number; }
