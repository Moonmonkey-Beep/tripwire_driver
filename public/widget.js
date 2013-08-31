var valueElement = element.find(".value");

scope.onData = function(data) {
  valueElement.html(data.DA);
}