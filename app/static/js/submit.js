"use strict";

function characterCounter(target, maxLength, currentLength, minLength) {
    /* Global character counter
     *
     * Parameters:
     * - target: string of target selector
     * - maxLength: integer of maximum character length
     * - currentLength: integer value of keyed in content
     * - minLength: integer of minimum character length (default = 0)
     *
     * Ex:
     * {
     *     target: "#note-content",
     *     charLength: 500,
     *     contentLength: $(this).val().length,
     *     minLength: 0
     * }
     *
     * */
    var length = maxLength - currentLength;
    minLength = (typeof minLength !== "undefined") ? minLength : 0;
    var s = length === 1 ? "" : "s";
    $(target).text(length + " character" + s + " remaining");
    if (length == 0) {
        $(target).css("color", "red");
    } else if (currentLength < minLength) {
        $(target).css("color", "red");
    }
    else {
        $(target).css("color", "black");
    }
}

$(document).ready(function () {
    // Initialize character counters
    $("#title").keyup(function () {
        characterCounter("#title-character-count", 150, $(this).val().length, 10);
    });
    $("#description").keyup(function () {
        characterCounter("#description-character-count", 300, $(this).val().length);
    });

    // Set MM/DD/YYYY mask on date published
    $("#date-published").mask("99/99/9999");

    // Set Parsley required validators
    var requiredFields = ["title", "agency", "subjects", "description", "date-published", "report-type", "language"];
    for (var i = 0; i < requiredFields.length; i++) {
        $("#" + requiredFields[i]).attr("data-parsley-required", "");
    }

    // Set custom Parlsey validators
    $("#date-published").attr("data-parsley-valid-date", "");
    $("#date-published").attr("data-parsley-future-date-invalid", "");

    // Custom validation messages
    $("#title").attr("data-parsley-required-message",
    "<i class=\"fas fa-exclamation-circle\"></i>&nbsp;<strong>Error, a title is required.</strong> Please type in a short title for your submission.");
    $("#agency").attr("data-parsley-required-message",
    "<i class=\"fas fa-exclamation-circle\"></i>&nbsp;<strong>Error, an agency is required.</strong> Please select an agency from the drop-down menu.");
    $("#subjects").attr("data-parsley-required-message",
    "<i class=\"fas fa-exclamation-circle\"></i>&nbsp;<strong>Error, a subject is required.</strong> Please select at least one subject.");
    $("#description").attr("data-parsley-required-message",
    "<i class=\"fas fa-exclamation-circle\"></i>&nbsp;<strong>Error, a description is required.</strong> Please type in a detailed description of your submission.");
    $("#date-published").attr("data-parsley-required-message",
    "<i class=\"fas fa-exclamation-circle\"></i>&nbsp;<strong>Error, date published is required.</strong> Please enter the date that the submission was published.");
    $("#report-type").attr("data-parsley-required-message",
    "<i class=\"fas fa-exclamation-circle\"></i>&nbsp;<strong>Error, a report type is required.</strong> Please select a report type from the drop-down menu.");
    $("#language").attr("data-parsley-required-message",
    "<i class=\"fas fa-exclamation-circle\"></i>&nbsp;<strong>Error, a language is required.</strong> Please select at least one language.");

    // initialize multiselect plugin for attendees
    $('#subjects').multiselect({
        maxHeight: 400,
        buttonText: function (options, select) {
            if (options.length === 0) {
                return 'None Selected';
            }
            else {
                var labels = [];
                options.each(function () {
                    if ($(this).attr('label') !== undefined) {
                        labels.push($(this).attr('label'));
                    }
                    else {
                        labels.push($(this).html());
                    }
                });
                return labels.join(', ') + '';
            }
        },
        enableCaseInsensitiveFiltering: true,
        includeResetOption: true,
        includeResetDivider: true,
        resetText: 'Clear all',
        buttonWidth: '100%'
    });
});