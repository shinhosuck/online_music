

// NAV MOBILE DROP AND CLOSE TOGGLE BUTTON
const faBars = document.querySelector(".fa-bars")
const faTimes = document.querySelector(".fa-times")
const navItems = document.querySelector(".nav-items")
const landingPageHeaderContainer = document.querySelector(".landing-page-header-container")
const landingPageHeaderAndText = document.querySelector(".landing-page-header-and-text")
const landingPage = document.querySelector(".landing-page")
const landingPageNavItems = document.querySelector(".landing-page-nav-items")

const userContainer = document.querySelector(".user-container")
const userWrapper = document.querySelector(".user-wrapper")

const userChevronDown = document.querySelector(".user-chevron-down")
const userChevronUp = document.querySelector(".user-chevron-up")

faBars.addEventListener("click", function(){
   navItems.classList.toggle("show-nav-items")
   faBars.classList.add("hide-fa-bars")
   faTimes.classList.add("show-fa-times")

   landingPageNavItems.style.height = "235px"

   if(landingPage || landingPageHeaderAndText) {
      landingPage.classList.remove("hide-overflow")
      landingPageHeaderAndText.classList.add("adjust-landing-page-header-and-text")
      if(window.innerHeight <= 650) {
         landingPageHeaderAndText.style.marginTop = "1.5rem"
      }
   }
   else{}
})

faTimes.addEventListener("click", ()=>{
   navItems.classList.toggle("show-nav-items")
   faBars.classList.remove("hide-fa-bars")
   faTimes.classList.remove("show-fa-times")


// remove user drop down menu on mobile
   navItems.classList.remove("show-nav-items1")
   userWrapper.classList.remove("show-user-wrapper")

   userChevronDown.style.display = "inline-block"
   userChevronUp.style.display = "none"
// end of mobile

   landingPageNavItems.style.height = "0"
   landingPageHeaderAndText.style.marginTop = "0"

   if(landingPage || landingPageHeaderAndText) {
      landingPage.classList.add("hide-overflow")
      landingPageHeaderAndText.classList.remove("adjust-landing-page-header-and-text")
   }
   else{}
})

window.addEventListener("resize", function(){
   if(window.innerWidth < 800 || window.innerWidth > 800) {
      navItems.classList.remove("show-nav-items")
      faTimes.classList.remove("show-fa-times")
      faBars.classList.remove("hide-fa-bars")

      landingPageNavItems.style.height = "0"

      if(landingPageHeaderAndText) {
         landingPageHeaderAndText.classList.remove("adjust-landing-page-header-and-text")
      }
      else{}

   }
})


// user drop down menu on mobile

// const userChevronDown = document.querySelector(".user-chevron-down")
// const userChevronUp = document.querySelector(".user-chevron-up")

userContainer.addEventListener("click", ()=>{
   userWrapper.classList.toggle("show-user-wrapper")
   navItems.classList.toggle("show-nav-items1")
   if(userWrapper.classList.contains("show-user-wrapper")) {
      userChevronDown.style.display = "none"
      userChevronUp.style.display = "inline-block"
   }
   else {
      userChevronDown.style.display = "inline-block"
      userChevronUp.style.display = "none"
   }
})
// end of mobile


// END OF NAV MOBILE DROP AND CLOSE TOGGLE BUTTON

const preventDefaults = document.querySelectorAll("#prevent-default")

preventDefaults.forEach((item)=>{
   item.addEventListener("click", (event)=>{
      event.preventDefault()
   })
})




/*============== 
SLIDE BANNER IMG
================*/

const sliderImgWrappers = document.querySelectorAll(".slider-img-wrapper")
// let nextBtn = document.querySelector("#next")
// let previousBtn = document.querySelector("#previous")
const circles = document.querySelectorAll(".circle")
let nextBtn = document.querySelector(".next")
let previousBtn = document.querySelector(".previous")

const mobileSliderImgWrappers = document.querySelectorAll(".mobile-slider-img-wrapper")
let mobileNextBtn = document.querySelector(".mobile-next")
let mobilePreviousBtn = document.querySelector(".mobile-previous")

let counter = 0

circles[counter].style.background = "rgb(255, 125, 51)"

previousBtn.addEventListener("click", ()=>{
   counter --
   slide()
})

nextBtn.addEventListener("click", ()=>{
   counter ++
   slide()
})

function slide(){
   circles.forEach(function (circle) {
      circle.style.background = "rgb(255, 255, 255)"
    })

   if(counter < 0) {
      counter = sliderImgWrappers.length -1
   }
   else if(counter > sliderImgWrappers.length -1){
      counter = 0
   }

   sliderImgWrappers.forEach(function (img) {
      img.style.transform = `translatex(-${counter * 100}%)`
      img.style.transition = "all 0.5s ease-in-out"
      circles[counter].style.background = "rgb(255, 125, 51)"
    })
}

circles.forEach(function (circle) {
   circle.addEventListener("click", function () {
      const newCircles = [...circles]
      newCircles.forEach(function (newCircle) {
      newCircle.style.background = "rgb(255, 255, 255)"
     })

     counter = newCircles.indexOf(circle)

     sliderImgWrappers.forEach(function (img) {
       img.style.transform = `translatex(-${counter * 100}%)`
       img.style.transition = "all 0.5s ease-in-out"
       newCircles[counter].style.background = "rgb(255, 125, 51)"
     })
 
   })
 })

// function autoSlide() {
//    circles.forEach(function (circle) {
//      circle.style.background = "rgb(255, 255, 255)"
//    })
//    if (counter > sliderImgWrappers.length - 1) {
//      counter = 0
//    }
//    sliderImgWrappers.forEach(function (img) {
//      img.style.transform = `translate(-${counter * 100}%)`
//      img.style.transition = "all 3s ease-in-out"
//      circles[counter].style.background = "rgb(255, 125, 51)"
//    })
//    counter++
//    setTimeout(autoSlide, 10000)
//  }
//  autoSlide()

/*======================
 END OF SLIDE BANNER IMG 
 =======================*/

/*======================
MOBILE SLIDER BANNER IMG
========================*/ 

mobilePreviousBtn.addEventListener("click", ()=>{
   counter --
   mobileSlide()
})

mobileNextBtn.addEventListener("click", ()=>{
   counter ++
   mobileSlide()
})

function mobileSlide(){

   if(counter < 0) {
      counter = mobileSliderImgWrappers.length -1
   }
   else if(counter > mobileSliderImgWrappers.length -1){
      counter = 0
   }

   mobileSliderImgWrappers.forEach(function (img) {
      img.style.transform = `translatex(-${counter * 100}%)`
      img.style.transition = "all 0.5s ease-in-out"
    })
}

/*=============================
END OF MOBILE SLIDER BANNER IMG
===============================*/ 

// NAV DROP DOWN MENU AUTO HIDE ON 530PX OR GREATER
window.addEventListener("scroll", function(){
   if(scrollY >= "530") {
      navItems.classList.remove("show-nav-items")
      faBars.classList.remove("hide-fa-bars")
      faTimes.classList.remove("show-fa-times")


   // remove user drop down menu on mobile
      navItems.classList.remove("show-nav-items1")
      userWrapper.classList.remove("show-user-wrapper")

      userChevronDown.style.display = "inline-block"
      userChevronUp.style.display = "none"
   // end of mobile

      console.log(scrollY)
   }
})

// END OF NAV DROP DOWN MENU AUTO HIDE ON 530PX OR GREATER
