## Workshop: Scraping webpages with R rvest package
# Prerequisite: Chrome browser, Selector Gadget

# install.packages("tidyverse")
library(tidyverse)
# install.packages("rvest")
library(rvest)

url <- 'https://en.wikipedia.org/wiki/List_of_countries_by_foreign-exchange_reserves'
#Reading the HTML code from the Wiki website
wikiforreserve <- read_html(url)

## Get the XPath data using Inspect element feature in Safari, Chrome or Firefox
## At Inspect tab, look for <table class=....> tag. Leave the table close
## Right click the table and Copy XPath, paste at html_nodes(xpath =)
foreignreserve <- wikiforreserve %>%
  html_nodes(xpath='//*[@id="mw-content-text"]/div/table[1]') %>%
  html_table()

fores = foreignreserve[[1]]
names(fores) <- c("Rank", "Country", "Forexres", "Date", "Change")
colnames(fores)

head(fores$Country, n=10)

## Clean up variables
## What type is Rank?
## How about Date?

# Remove trailing notes in Date variable
library(stringr)
fores$newdate = str_split_fixed(fores$Date, "\\[", n = 2)[, 1]


write.csv(fores, "fores.csv", row.names = FALSE)

## Using class element name and magrittr
# install.packages("magrittr")
library(magrittr)

# Use forward-pipe operator to chain commands
table <- wikiforreserve %>%
  html_nodes("table.wikitable") %>%
  html_table(header=T)
table <- table[[1]] # List to dataframe

url1 = "https://www.imdb.com/search/title/?release_date=2019-01-01,2020-01-01"
imdb2019 <- read_html(url1)
rank_data_html <- html_nodes(imdb2019,'.text-primary')
rank_data <- as.numeric(html_text(rank_data_html))
head(rank_data, n = 10)
title_data_html <- html_nodes(imdb2019,'.lister-item-header a')
title_data <- html_text(title_data_html)

head(title_data, n =20)


