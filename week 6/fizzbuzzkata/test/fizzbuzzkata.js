const assert = require('chai').assert
const app = require('../fizzbuzz')

describe('App', function(){
    it('app should return fizz', function(){
        assert.equal(app(3), 'fiz')
    })
    it('app should return buzz', function(){
        assert.equal(app(5), 'buz')
    })
    it('app should return fizzbuzz', function(){
        assert.equal(app(15), 'fizzbu1z')
    })
})