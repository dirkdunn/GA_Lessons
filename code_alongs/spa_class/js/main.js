// 9f7fe3b0ceb0a7cf1e86812469152bc0
$(document).ready(function(){
  var weatherApiKey = '9f7fe3b0ceb0a7cf1e86812469152bc0',
    defaultCity = 'Austin';

  function getWeatherData(city){
    // Get weather data
    $.get('http://api.openweathermap.org/data/2.5/weather?q='+city+'&units=imperial&APPID='+weatherApiKey,function(response){
      console.log('Weather Response: ', response)
      var city = response.name,
        temperature = response.main.temp + 'º',
        humidity = response.main.humidity + '%',
        description = response.weather[0].description;

      $('.results').find('.results-city').text(city).closest('.results')
        .find('.temperature-container .temperature').text(temperature).closest('.results')
        .find('.humidity-container .humidity').text(humidity).closest('.results')
        .find('.description-container .description').text(description);

    });
  };

  function setHandlers(){
    $('form.getWeatherData').on('submit',function(e){
      e.preventDefault();
      var city = $(this).find('.weather-city').val();
      console.log('city: ', city);
      getWeatherData(city);
    });
  };

  function main(){
    getWeatherData(defaultCity);
    setHandlers();
  };

  main();
});
