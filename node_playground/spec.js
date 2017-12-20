// Simple Test with Page Object
var angularHomepage = require('./angular_homepage');

describe('angularjs homepage', function() {
    it('should greet the named user', function() {
        // Load the AngularJS homepage.
        angularHomepage.get();

        // Set Name to test value
        angularHomepage.setName('Paul');

        // Grab Greeting from Page Object and compare to expected result
        expect(angularHomepage.getGreeting()).toEqual('Hello Paul!');
    });
});

// Simple Test without Page Object
describe('angularjs homepage', function() {
    it('should greet the named user', function() {
        // Load the AngularJS homepage.
        browser.get('http://www.angularjs.org');

        // Find the element with ng-model matching 'yourName' - this will
        // find the <input type="text" ng-model="yourName"/> element - and then
        // type 'Julie' into it.
        element(by.model('yourName')).sendKeys('Julie');

        // Find the element with binding matching 'yourName' - this will
        // find the <h1>Hello {{yourName}}!</h1> element.
        var greeting = element(by.binding('yourName'));

        // Assert that the text element has the expected value.
        // Protractor patches 'expect' to understand promises.

        expect(greeting.getText()).toEqual('Hello Julie!');
    });
});