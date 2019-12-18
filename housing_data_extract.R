setwd('~/Downloads/550project')
dataset <- read.csv("Raw_Data.csv")
library(dplyr)
x <- c(90012,90031,90032,90022,91754,91755,90640,91107,91775,91108,91006,91024,91016,91706,91010,91702,91722,91741,91740)
data_90012 <- dataset[dataset$ZipCode == 90012,]
data_90031 <- dataset[dataset$ZipCode == 90031,]
data_90032 <- dataset[dataset$ZipCode == 90032,]
data_90022 <- dataset[dataset$ZipCode == 90022,]
data_91754 <- dataset[dataset$ZipCode == 91754,]
data_91755 <- dataset[dataset$ZipCode == 91755,]
data_90640 <- dataset[dataset$ZipCode == 90640,]
data_91107 <- dataset[dataset$ZipCode == 91107,]
data_91775 <- dataset[dataset$ZipCode == 91775,]
data_91108 <- dataset[dataset$ZipCode == 91108,]
data_91106 <- dataset[dataset$ZipCode == 91106,]
data_91024 <- dataset[dataset$ZipCode == 91024,]
data_91016 <- dataset[dataset$ZipCode == 91016,]
data_91706 <- dataset[dataset$ZipCode == 91706,]
data_91010 <- dataset[dataset$ZipCode == 91010,]
data_91702 <- dataset[dataset$ZipCode == 91702,]
data_91722 <- dataset[dataset$ZipCode == 91722,]
data_91741 <- dataset[dataset$ZipCode == 91741,]
data_91740 <- dataset[dataset$ZipCode == 91740,]

y <- c(90064,90249,90808,90630,90621,90631,92805,90068,91506,91762)
z <- c(91773,91750,91711,91767,91762)

data_90064 <- dataset[dataset$ZipCode == "90064",]
data_90249 <- dataset[dataset$ZipCode == "90249",]
data_90808 <- dataset[dataset$ZipCode == "90808",]
data_90630 <- dataset[dataset$ZipCode == "90630",]
data_90621 <- dataset[dataset$ZipCode == "90621",]
data_90631 <- dataset[dataset$ZipCode == "90631",]
data_92805 <- dataset[dataset$ZipCode == "92805",]
data_90068 <- dataset[dataset$ZipCode == "90068",]
data_91506 <- dataset[dataset$ZipCode == "91506",]
data_91762 <- dataset[dataset$ZipCode == "91762",]
data_91773 <- dataset[dataset$ZipCode == "91773",]
data_91750 <- dataset[dataset$ZipCode == "91750",]
data_91711 <- dataset[dataset$ZipCode == "91711",]
data_91767 <- dataset[dataset$ZipCode == "91767",]
data_91762 <- dataset[dataset$ZipCode == "91762",]


new_table <- data_90064$Month
new_table <- lapply(new_table, toString)
new_table <- substr(new_table, 1, 11)
new_table <- rev(new_table)


a.price <- rev(data_91762$Avg.Listing.Price)
new_dataset <- rbind(new_dataset, a.price)

new_dataset_2 <- new_dataset
new_dataset_2 <- as.data.frame(new_dataset_2)
new_dataset_2 <- new_dataset_2[-c(1)]
names(new_dataset_2) <- as.matrix(new_dataset_2[1,])
new_dataset_2 <- new_dataset_2[-c(1),]
row.names(new_dataset_2) <- z
write.csv(new_dataset_2, file = "Test_Average_Price.csv")

# check_zipcode <- dataset[dataset$ZipCode == "90068",]

