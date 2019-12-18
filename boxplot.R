setwd("~/Downloads/550project")
data <- read.csv("rental_diff_boxplot.csv")
training <- data$Training.Group
control <- data$Control.Group
control <- control[1:10]
boxplot(training, control, 
        main = "Traning Control for Comparision",
        names = c("Training", "Control"),
        horizontal = TRUE)

        