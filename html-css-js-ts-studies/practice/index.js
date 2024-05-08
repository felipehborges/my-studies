"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var Philosopher = /** @class */ (function () {
    function Philosopher(first, last) {
        this.first = first;
        this.last = last;
    }
    return Philosopher;
}());
var philosopher1 = new Philosopher('Immanuel', 'Kant');
console.log(philosopher1);
