// conf.js
exports.config = {

    // Framework to use
    framework: 'jasmine',

    // Start the Selenium Server before running specs files
    seleniumServerJar: 'C:\\Users\\u0172346\\AppData\\Roaming\\npm\\node_modules\\protractor\\node_modules\\webdriver-manager\\selenium\\selenium-server-standalone-3.8.1.jar',
    seleniumPort: 4444,

    // The address of a running selenium server if started separately
    // with webdriver-manager start
    // seleniumAddress: 'http://localhost:4444/wd/hub',

    // Credentials if pointing to BrowserStack's Remote Selenium Server
    // browserstackUser: ''
    // browserstachKey: ''

    // List of test spec files to run (relative to conf.js)
    specs: ['spec.js'],

    // Browser to be used for test, uses Chrome
    capabilities: {
        browserName: 'chrome',
        'chromeOptions': {
            'args': ['start-maximized=true',
                     'disable-extensions=true',
                     'test-type=true']
        }
    }

    // For multiple browsers running concurrently
    //     multiCapabilities: [{
    //     browserName: 'firefox'
    //  }, {
    //      browserName: 'chrome'
    //  }]
};