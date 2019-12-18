setwd('~/Downloads/550project')
rental_data <- read.csv("rental_price.csv")
library(dplyr)
library(stringr)
training_zipcode <- c(90012,90031,90032,90022,91754,91755,90640,91107,91775,91108,91006,91024,91016,91706,91010,91702,91722,91741,91740)
training_area <- filter(rental_data, str_detect(RegionName, paste(training_zipcode, collapse="|")))
training_area <- training_area[c(2,28:116)]
training_area <- training_area[c(1:85)]
rowName <- training_area[,c(1)]
row.names(training_area) <- rowName
training_area <- training_area[-c(1)]
colNames <- names(training_area)
colNames <- substr(colNames, 2, 8)
colNames <- str_replace(colNames, '\\.', "-")
colNames <- paste0(colNames, "-01")
names(training_area) <- colNames
write.csv(training_area, "rental_price_training.csv")

control_zipcode <- c(91773,91750,91711,91767,91762)
control_area <- filter(rental_data, str_detect(RegionName, paste(control_zipcode, collapse="|")))
control_area <- control_area[c(2,28:116)]
control_area <- control_area[c(1:85)]

c.rowName <- control_area[,c(1)]
row.names(control_area) <- c.rowName
control_area <- control_area[-c(1)]
colNames <- names(control_area)
colNames <- substr(colNames, 2, 8)
colNames <- str_replace(colNames, '\\.', "-")
colNames <- paste0(colNames, "-01")
names(control_area) <- colNames
write.csv(control_area, "Rental_Price_Test.csv")
