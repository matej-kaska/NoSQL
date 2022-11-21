function reduce(name, values) {
    var emailDups = 0;
    var ujep = false
    var seznam = false
    for (var index = 0; index < values.length; ++index) {
        emailDups = emailDups + 1
    }
    if(name.substring(name.length - 8) == "@ujep.cz") {
        ujep = true
    }
    if(name.substring(name.length - 10) == "@seznam.cz") {
        seznam = true
    }
    return {"emailDups": emailDups, "ujep": ujep, "seznam": seznam};
    
}