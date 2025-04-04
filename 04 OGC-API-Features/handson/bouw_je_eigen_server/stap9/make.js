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

const serviceTitle = "amstelveen OGC API Feature server";
const serviceDescription = "Access to data in the city of amstelveen via a Web API that conforms to the OGC API Features specification.";
const serviceUrl = "http://localhost:8080/demoservice/v1/";

function landingPageJSON() {
    var json = header(serviceTitle, serviceDescription);
    
    json.links.push(link(serviceUrl,                 "self",         "application/json", "this document"));
    json.links.push(link(serviceUrl + "api",         "service-desc", "application/vnd.oai.openapi+json;version=3.0", "the API definition"));
    json.links.push(link(serviceUrl + "api.html",    "service-doc",  "text/html",        "the API documentation"));
    json.links.push(link(serviceUrl + "conformance", "conformance",  "application/json", "OGC API conformance classes implemented by this server"));
    json.links.push(link(serviceUrl + "collections", "data",         "application/json", "Information about the feature collections"));
    
    return json;
}

function landingPageHTML() {
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


//-------------------------------------------------------------------------------------

function collectionsJSON(collections) {
    var json = {}

    json.links = []
    json.links.push(link(serviceUrl + "collections", "self", "application/json", "Metadata about the feature collections"));
    
    json.collections = [];

    for (var collectionId in collections) {
       var item = header(collectionId, collectionId);
       item.links.push(link(serviceUrl + "collections/" + collectionId + "/items", "item", "application/json", collectionId));
       json.collections.push(item);
    };

    return json;
}

function collectionsHTML(collections) {

    var items = [];
    for (var collectionId in collections) {
        var item = {};
        item.url = serviceUrl;
        item.title = collectionId;
        items.push(item);
    };

    var tmpl = pug.compileFile(__dirname + '/collections.pug'),
    renderedHtml = tmpl({
        collections: items,
    });
    
    return renderedHtml;
}

function collections(t, collections) {
    if (t == "json")
        return collectionsJSON(collections);
    return collectionsHTML(collections);
}

//-------------------------------------------------------------------------------------

function collectionJSON(collectionId) {
    var json = {}

    json.links = []
    json.links.push(link(serviceUrl + "collections", "self", "application/json", "Metadata about the feature collections"));
    
    json.collections = [];

    var item = header(collectionId, collectionId);
    item.links.push(link(serviceUrl + "collections/" + collectionId + "/items", "item", "application/json", collectionId));
    json.collections.push(item);

    return json;
}

function collectionHTML(collectionId) {

    var item = {};
    item.url = serviceUrl;
    item.title = collectionId;

    var tmpl = pug.compileFile(__dirname + '/collection.pug'),
    renderedHtml = tmpl({
        collection: item,
    });
    
    return renderedHtml;
}

function collection(t, collectionId) {
    if (t == "json")
        return collectionJSON(collectionId);
    return collectionHTML(collectionId);
}

//-------------------------------------------------------------------------------------

function itemsJSON(collectionId, geojson) {
    return JSON.parse(JSON.stringify(geojson));
}

function itemsHTML(collectionId, geojson) {

    var item = {};
    item.url = serviceUrl;
    item.title = collectionId;
    item.geojson = JSON.stringify(geojson);

    var tmpl = pug.compileFile(__dirname + '/items.pug'),
    renderedHtml = tmpl({
        collection: item,
    });
    
    return renderedHtml;
}

function items(t, collectionId, geojson) {
    if (t == "json")
        return itemsJSON(collectionId, geojson);
    return itemsHTML(collectionId, geojson);
}

//-------------------------------------------------------------------------------------

module.exports = { landingPage, collections, collection, items }
