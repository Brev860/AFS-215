const assert = require('chai').assert
const app = require('../fizzbuzz')

describe('App', function(){
    it('app should return 1', function(){
        assert.equal(app(1), '1')
    })
    it('app should return 2', function(){
        assert.equal(app(2), '2')
    })
})