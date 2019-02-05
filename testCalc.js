import { calculator } from './app'

assert(calculator.add(4, 5) == 9, 'testing add')
assert(calculator.sub(5, 3) == 2, 'testing sub')
assert(calculator.mul(4, 5) == 20, 'testing mul')
assert(calculator.div(10, 5) == 2, 'testing div')