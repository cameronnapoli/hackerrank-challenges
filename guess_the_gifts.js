/*
You will be given a wishlist (array), containing all possible items. Each item is in the format: {name: "toy car", size: "medium", clatters: "a bit", weight: "medium"} (Ruby version has an analog hash structure, see example below)

You also get a list of presents (array), you see under the christmas tree, which have the following format each: {size: "small", clatters: "no", weight: "light"}

Your task is to create a list of all possible presents you might get.
*/

Array.prototype.removeDuplicates = function() {
    var result = [], freq = {};
    for(var i = 0; i < this.length; i++) { freq[this[i]] = 0; }
    this.splice(0, this.length); // clear array
    for (var f in freq) { this.push(f); }
    return this;
}
function guessGifts(wishlist, presents) {
    return presents.map(function(present) {
        return wishlist.filter(function(obj) {
                return (obj.size == present.size) &&
                       (obj.clatters == present.clatters) &&
                       (obj.weight == present.weight);
            }).map(function(wishlistObj) { // map names to output
                return wishlistObj.name;
            });
    }).reduce(function(a, b) { return a.concat(b); }, []).removeDuplicates(); // flatten
}

/*
var wishlist = [
    {name: "Mini Puzzle", size: "small", clatters: "yes", weight: "light"},
    {name: "Toy Car", size: "medium", clatters: "a bit", weight: "medium"},
    {name: "Card Game", size: "small", clatters: "no", weight: "light"}
];

var presents = [
    {size: "medium", clatters: "a bit", weight: "medium"},
    {size: "small", clatters: "yes", weight: "light"}
];

guessGifts(wishlist, presents); // must return ["Toy Car", "Mini Puzzle"]
*/
