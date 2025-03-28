// var swig = require('swig-templates');
var pug = require('pug');

function header(title, description) {
    var header = {};
    header.title = title;
    header.description = description;
    header.links = [];

    return header;
}

function link(href, rel, type, title) {
    var item = {};
    item.href = href;
    item.rel = rel;
    item.type = type;
    item.title = title;

    return item;
}

const serviceTitle = "Amstelveen OGC API Feature server";
const serviceDescription = "Access to data in the city of amstelveen via a Web API that conforms to the OGC API Features specification.";
const serviceUrl = "http://localhost:8080/demoservice/v1";

function landingPageJSON() {
    var landingPage = header(serviceTitle, serviceDescription);
    
    landingPage.links.push(link(serviceUrl,                 "self",         "application/json", "this document"));
    landingPage.links.push(link(serviceUrl + "api",         "service-desc", "application/vnd.oai.openapi+json;version=3.0", "the API definition"));
    landingPage.links.push(link(serviceUrl + "api.html",    "service-doc",  "text/html",        "the API documentation"));
    landingPage.links.push(link(serviceUrl + "conformance", "conformance",  "application/json", "OGC API conformance classes implemented by this server"));
    landingPage.links.push(link(serviceUrl + "collections", "data",         "application/json", "Information about the feature collections"));
    
    return landingPage;
}

function landingPageHTML() {
    // var tmpl = swig.compileFile(__dirname + '/landingPage.template'),
    // renderedHtml = tmpl({
    //     title: serviceTitle,
    //     url: serviceUrl,
    // });
    var tmpl = pug.compileFile(__dirname + '/landingPage.pug'),
    renderedHtml = tmpl({
            title: serviceTitle,
            description: serviceDescription,
            url: serviceUrl
        });
    
    return renderedHtml;
}

function landingPage(t) {
    if (t == "json")
        return landingPageJSON();
    return landingPageHTML();
}

module.exports = { landingPage }
