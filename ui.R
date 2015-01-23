library(shiny)
library(rjson)

# Define UI for application that draws a histogram
shinyUI(fluidPage(
  
  # Application title
  titlePanel('mineBalls'),
  #'twitter sentiment analyser',
  
  # Sidebar with a dropdown to select match, and entry box for bandwidth
  sidebarLayout(
    sidebarPanel(
      uiOutput("matchChooser"),
      uiOutput("tagChooser"),
      checkboxInput('plotByTag',
                    'Enable',
                    value=FALSE),
      sliderInput('f',
                  h4('Smoothness'),
                  min=0.01,
                  max=1,
                  value=0.05)
      ),    
    
    mainPanel (
      h3(textOutput("scoreboard"), style='text-align:center;'),
      plotOutput("sentimentPlot")
      #textOutput("teams"),
      #textOutput("testtext")
      )
    )
  ))