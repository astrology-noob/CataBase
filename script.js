// $( function() {
//     var availableTags = [ 
//         {% for breed in breeds_options %}
//             "{{breed['name']}}",
//         {% endfor %}
//         ];
//     $( "#breeds" ).autocomplete({
//     source: availableTags
//     });
// } );

$( function() {
    var availableBreeds = [ 
    {% for breed in breed_options %}
        "{{breed['name']}}",
    {% endfor %}
    ];

var availableEyeColors = [
    {% for eye_color in eye_color_options %}
        "{{eye_color['name']}}",
    {% endfor %}
    ];

var availableFurColors = [
    {% for fur_color in fur_color_options %}
        "{{fur_color['name']}}",
    {% endfor %}
    ];

var availableCountries = [
    {% for country in country_options %}
        "{{country['name']}}",
    {% endfor %}
    ];

$( "#breed" ).autocomplete({
source: availableBreeds
});

$( ".eye_color" ).autocomplete({
source: availableEyeColors
});

$( "#fur_color" ).autocomplete({
source: availableFurColors
});

$( "#country" ).autocomplete({
source: availableCountries
});

} );