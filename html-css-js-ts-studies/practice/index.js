"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var System = /** @class */ (function () {
    function System(programmingLanguages, programmers, paymentSystem) {
        this.programmingLanguages = programmingLanguages;
        this.programmers = programmers;
        this.paymentSystem = paymentSystem;
    }
    return System;
}());
var sci2 = new System(['JavaScript', 'TypeScript'], ['Brendan Eich', 'Anders Hejlsberg'], true);
console.log(sci2);
console.log(sci2.programmingLanguages);
console.log(sci2.programmers);
console.log(sci2.paymentSystem);
