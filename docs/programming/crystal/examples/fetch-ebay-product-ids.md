The goal of this sample is to demonstrate fetching HTML data from a page (en eBay search listing), parsing the HTML content using a 3rd party library[^myhtml], and looking for a specific attribute within the content (`listingId`). The elements that have it contain IDs to the products that apear on the given listing page. We would finally map those out, and turn the resulting array into a set (`to_s`) in order to remove duplicates.

```crystal
require "http/client"
require "myhtml"

module Bayhunt
  res = HTTP::Client.get "https://www.ebay.com/sch/i.html?_nkw=iphone+xr"
  parser = Myhtml::Parser.new(res.body)

  listing_ids = parser.css("[listingId]")
    .to_a
    .map do |it|
      it.attributes["listingid"].to_i64
    end.to_s

  # or, use the shorter-form version (`&`) if there is only one argument passed to the block
  listing_ids = parser.css("[listingId]")
    .to_a
    .map(&.attributes["listingid"].to_i64)
    .to_s

  p listing_ids
end

```

[^myhtml]: [myhtml - Fast HTML5 Parser, Css selectors | GtiHub](https://github.com/kostya/myhtml)
[^http_client]: [class HTTP::Client | Crystal API Reference](https://crystal-lang.org/api/0.24.2/HTTP/Client.html)
[^blocks]: [Blocks and Procs | Crystal Docs](https://crystal-lang.org/reference/syntax_and_semantics/blocks_and_procs.html)
