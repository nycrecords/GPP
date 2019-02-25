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
    $("#date_published").mask("99/99/9999");
});