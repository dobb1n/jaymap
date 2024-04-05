# JayMap - a project which overlays Guardian restaurant reviews onto google maps

## What is this?
I love [Jay Rayner's restaurant reviews in the guardian](https://www.theguardian.com/food/series/jay-rayner-on-restaurants). when travelling, i would always try to find a restaurant he had reviewed close to where I was staying (fairly obviously, one which got an ok review). You can absolutely google for jay rayner and the city it is you are in, but then you have to know where in the city the restaurant is, or do a follow up google (or be prepared to get a cab). What i wanted was an overlay on google maps which could show me relative to me where the restaurants were, so i could pick one which i could walk to. 

The code in here calls the guardian API for anything matching the tag *food/series/jay-rayner-on-restaurants*. That gives us a list of URLS which we can then visit and regex the postcode out of. The link and postcode gets saved to a csv which we then manually overlay onto google maps. 

## Where can i see this map then? 
https://www.google.com/maps/d/edit?mid=1gIdAmI0MwnaKkCN4hQmrhtEsjOWTJuAf&usp=sharing

## There is a restaurant missing
There is, yes. This is most likely because not all reviews have a postcode in, and thats what this code is looking for. I plan to extend it to try to work out the address from the page without the postcode. This seems to be almost all restaurants from before march 2016. 

## why isnt this all the guardian food critics?
It could be made to be. I will do different overlays for Grace and any other ones. 

## todo
firebase app
make cloud function to collect the stuff and stick it in a database
