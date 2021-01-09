<template>
  <div class="player">
<svg class="svg-icon__sprite" xmlns="http://www.w3.org/2000/svg">
  <symbol id="i-maximize" viewbox="0 0 32 32">
    <polyline points="1.9,15.6 3.3,2.9 16,1.5 "></polyline>
    <line x1="3.3" y1="2.9" x2="29.4" y2="29.1"></line>
    <polyline points="30.8,16.4 29.4,29.1 16.7,30.5 "></polyline>
  </symbol>
  <symbol id="i-search" viewbox="0 0 32 32">
    <circle cx="14" cy="14" r="12"></circle>
    <path d="M23 23 L30 30"></path>
  </symbol>
  <symbol id="i-close" viewbox="0 0 32 32">
    <path d="M2 30 L30 2 M30 30 L2 2"></path>
  </symbol>
  <symbol id="i-plus" viewbox="0 0 32 32">
    <path d="M16 2 L16 30 M2 16 L30 16"></path>
  </symbol>
  <symbol id="i-minus" viewbox="0 0 32 32">
    <path d="M2 16 L30 16"></path>
  </symbol>
  <symbol id="i-play" viewbox="0 0 32 32">
    <path d="M10 2 L10 30 24 16 Z"></path>
  </symbol>
  <symbol id="i-pause" viewbox="0 0 32 32">
    <path d="M23 2 L23 30 M9 2 L9 30"></path>
  </symbol>
  <symbol id="i-backwards" viewbox="0 0 32 32">
    <path d="M16 2 L2 16 16 30 16 16 30 30 30 2 16 16 Z"></path>
  </symbol>
  <symbol id="i-forwards" viewbox="0 0 32 32">
    <path d="M16 2 L30 16 16 30 16 16 2 30 2 2 16 16 Z"></path>
  </symbol>
  <symbol id="i-star" viewbox="0 0 32 32">
    <path d="M16 2 L20 12 30 12 22 19 25 30 16 23 7 30 10 19 2 12 12 12 Z"></path>
  </symbol>
  <symbol id="i-checkmark" viewbox="0 0 32 32">
    <path d="M2 20 L12 28 30 4"></path>
  </symbol>
  <symbol id="i-chevron-top" viewbox="0 0 32 32">
    <path d="M30 20 L16 8 2 20"></path>
  </symbol>
  <symbol id="i-chevron-right" viewbox="0 0 32 32">
    <path d="M12 30 L24 16 12 2"></path>
  </symbol>
  <symbol id="i-chevron-bottom" viewbox="0 0 32 32">
    <path d="M30 12 L16 24 2 12"></path>
  </symbol>
  <symbol id="i-chevron-left" viewbox="0 0 32 32">
    <path d="M20 30 L8 16 20 2"></path>
  </symbol>
  <symbol id="i-arrow-top" viewbox="0 0 32 32">
    <path d="M6 10 L16 2 26 10 M16 2 L16 30"></path>
  </symbol>
  <symbol id="i-arrow-right" viewbox="0 0 32 32">
    <path d="M22 6 L30 16 22 26 M30 16 L2 16"></path>
  </symbol>
  <symbol id="i-arrow-bottom" viewbox="0 0 32 32">
    <path d="M6 22 L16 30 26 22 M16 30 L16 2"></path>
  </symbol>
  <symbol id="i-arrow-left" viewbox="0 0 32 32">
    <path d="M10 6 L2 16 10 26 M2 16 L30 16"></path>
  </symbol>
  <symbol id="i-caret-top" viewbox="0 0 32 32">
    <path d="M30 22 L16 6 2 22 Z"></path>
  </symbol>
  <symbol id="i-caret-right" viewbox="0 0 32 32">
    <path d="M10 30 L26 16 10 2 Z"></path>
  </symbol>
  <symbol id="i-caret-bottom" viewbox="0 0 32 32">
    <path d="M30 10 L16 26 2 10 Z"></path>
  </symbol>
  <symbol id="i-caret-left" viewbox="0 0 32 32">
    <path d="M22 30 L6 16 22 2 Z"></path>
  </symbol>
  <symbol id="i-start" viewbox="0 0 32 32">
    <path d="M8 2 L8 16 22 2 22 30 8 16 8 30"></path>
  </symbol>
  <symbol id="i-end" viewbox="0 0 32 32">
    <path d="M24 2 L24 16 10 2 10 30 24 16 24 30"></path>
  </symbol>
  <symbol id="i-eject" viewbox="0 0 32 32">
    <path d="M30 18 L16 5 2 18Z M2 25 L30 25"></path>
  </symbol>
  <symbol id="i-mute" viewbox="0 0 32 32">
    <path d="M20 16 C20 8 15 2 15 2 L8 10 2 10 2 22 8 22 15 30 C15 30 20 24 20 16 Z"></path>
  </symbol>
  <symbol id="i-volume" viewbox="0 0 32 32">
    <path d="M20 16 C20 8 15 2 15 2 L8 10 2 10 2 22 8 22 15 30 C15 30 20 24 20 16 Z M21 2 C21 2 25 6 25 16 25 26 21 30 21 30 M27 4 C27 4 30 8 30 16 30 24 27 28 27 28"></path>
  </symbol>
  <symbol id="i-ban" viewbox="0 0 32 32">
    <circle cx="16" cy="16" r="14"></circle>
    <path d="M6 6 L26 26"></path>
  </symbol>
  <symbol id="i-options" viewbox="0 0 32 32">
    <path d="M28 6 L4 6 M28 16 L4 16 M28 26 L4 26 M24 3 L24 9 M8 13 L8 19 M20 23 L20 29"></path>
  </symbol>
  <symbol id="i-settings" viewbox="0 0 32 32">
    <path d="M13 2 L13 6 11 7 8 4 4 8 7 11 6 13 2 13 2 19 6 19 7 21 4 24 8 28 11 25 13 26 13 30 19 30 19 26 21 25 24 28 28 24 25 21 26 19 30 19 30 13 26 13 25 11 28 8 24 4 21 7 19 6 19 2 Z"></path>
    <circle cx="16" cy="16" r="4"></circle>
  </symbol>
  <symbol id="i-heart" viewbox="0 0 32 32">
    <path d="M4 16 C1 12 2 6 7 4 12 2 15 6 16 8 17 6 21 2 26 4 31 6 31 12 28 16 25 20 16 28 16 28 16 28 7 20 4 16 Z"></path>
  </symbol>
  <symbol id="i-clock" viewbox="0 0 32 32">
    <circle cx="16" cy="16" r="14"></circle>
    <path d="M16 8 L16 16 20 20"></path>
  </symbol>
  <symbol id="i-menu" viewbox="0 0 32 32">
    <path d="M4 8 L28 8 M4 16 L28 16 M4 24 L28 24"></path>
  </symbol>
</svg>

  <section class="section flexy__item flexy--column flexy--items-center space--big">

    <article class="section__article flexy__item flexy--column flexy--items-center">
      <header class="header accessible-hide">
        <h3>A skinnable video player.</h3>
      </header>
      <div class="video flexy__item">
        <video class="video__player" id="video__player" autoplay="autoplay" preload="metadata">
          <source src="" type="video/mp4"/>
        </video>
        <div class="video__control flexy__item">
          <div class="video__duration flexy__item flexy--items-center tooltip" id="video__duration" data-tooltip-content="Duration">00:00:00</div>
          <ul class="flexy__item">
            <li class="video__control__button tooltip" id="video__start" data-tooltip-content="Start">
              <svg class="svg-icon stroke--white" fill="none">
                <use class="use" xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#i-start"></use>
              </svg>
            </li>
            <li class="video__control__button tooltip" id="video__play" data-tooltip-content="Play">
              <svg class="svg-icon stroke--white" fill="none">
                <use class="use" xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#i-play"></use>
              </svg>
            </li>
            <li class="video__control__button tooltip" id="video__pause" data-tooltip-content="Pause">
              <svg class="svg-icon stroke--white" fill="none">
                <use class="use" xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#i-pause"></use>
              </svg>
            </li>
            <li class="video__control__button tooltip" id="video__end" data-tooltip-content="End">
              <svg class="svg-icon stroke--white" fill="none">
                <use class="use" xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#i-end"></use>
              </svg>
            </li>
          </ul>
          <div class="video__control__button video__track flexy__child flexy__item flexy--items-center tooltip" data-tooltip-content="Track">
            <input class="video__track__range flexy__child" id="video__track" type="range" step="1" min="0" max="0" value="0"/>
          </div>
          <div class="video__control__button volume flexy__item tooltip" data-tooltip-content="Volume">
            <svg class="svg-icon stroke--white" id="video__sound" fill="none">
              <use class="use" xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#i-volume"></use>
            </svg>
            <div class="video__track__range__sound">
              <input class="video__track__range" id="sound__track" type="range" step="1" min="0" max="10" value="10"/>
            </div>
          </div>
          <div class="video__control__button tooltip" id="video__fullScreen" data-tooltip-content="Maximize">
            <svg class="svg-icon stroke--white" fill="none">
              <use class="use" xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#i-maximize"></use>
            </svg>
          </div>
        </div>
      </div>
    </article>
  </section>

</div>

</template>

<script>
export default {
  name: 'MoviePlayer',

}

</script>
<style scoped>
html, body, div, span, applet, object, iframe,
h1, h2, h3, h4, h5, h6, p, blockquote, pre,
a, abbr, acronym, address, big, cite, code,
del, dfn, em, img, ins, kbd, q, s, samp,
small, strike, strong, sub, sup, tt, var,
b, u, i, center,
dl, dt, dd, ol, ul, li,
fieldset, form, label, legend,
table, caption, tbody, tfoot, thead, tr, th, td,
article, aside, canvas, details, embed,
figure, figcaption, footer, header, hgroup,
menu, nav, output, ruby, section, summary,
time, mark, audio, video {
  margin: 0;
  padding: 0;
  border: 0;
  font: inherit;
  font-size: 100%;
  vertical-align: baseline;
}

html {
  line-height: 1;
}

ol, ul {
  list-style: none;
}

table {
  border-collapse: collapse;
  border-spacing: 0;
}

caption, th, td {
  text-align: left;
  font-weight: normal;
  vertical-align: middle;
}

q, blockquote {
  quotes: none;
}
q:before, q:after, blockquote:before, blockquote:after {
  content: "";
  content: none;
}

a img {
  border: none;
}

article, aside, details, figcaption, figure, footer, header, hgroup, main, menu, nav, section, summary {
  display: block;
}

@font-face {
  font-family: 'Playfair Display';
  src: url();
  font-weight: normal;
  font-style: normal;
}
@font-face {
  font-family: 'Sintony Bold';
  src: url();
  font-weight: normal;
  font-style: normal;
}
@font-face {
  font-family: 'Sintony';
  src: url();
  font-weight: normal;
  font-style: normal;
}
/* COLORS */
/* ACELERATIONS */
/* TIMING */
/* SIZES */
/* FLEXY BEHAVIOR */
.flexy__item {
  display: flex;
  flex-wrap: nowrap;
}
.flexy__child {
  flex-grow: 1;
  flex-shrink: 1;
  flex-basis: 0;
}
.flexy__child--fill {
  flex-basis: 100%;
}
.flexy__item, .flexy_child {
  box-sizing: border-box;
}
.flexy--row {
  flex-direction: row;
}
.flexy--column {
  flex-direction: column;
}
.flexy--between {
  justify-content: space-between;
}
.flexy--around {
  justify-content: space-around;
}
.flexy--justify-start {
  justify-content: flex-start;
}
.flexy--justify-end {
  justify-content: flex-end;
}
.flexy--justify-center {
  justify-content: center;
}
.flexy--items-center {
  align-items: center;
}
.flexy--self-end {
  align-self: flex-end;
}
.flexy--reverse-column {
  flex-direction: column-reverse;
}
.flexy--reverse-row {
  flex-direction: row-reverse;
}

html,
body,
main {
  height: 100vh;
  width: 100vw;
  box-sizing: border-box;
  -webkit-overflow-scrolling: touch;
}

body {
  color: #FFFFFF;
  font-family: 'Sintony', sans-serif;
  -webkit-font-smoothing: antialiased;
  -webkit-tap-highlight-color: transparent;
  line-height: 1.4em;
  background-image: linear-gradient(135deg, #FF5572, #FF7555);
  overflow: hidden;
}

main {
  position: relative;
  padding: 2.8em;
  z-index: 2;
  overflow: auto;
}
@media (max-width: 40em) {
  main {
    padding: 0;
  }
}

.section {
  width: 100%;
}
.section > .header {
  margin-bottom: 1.4em;
}
.section__article {
  width: 100%;
  box-sizing: border-box;
  color: #404040;
}

em,
strong {
  font-weight: 700;
}

h1, h2, h3, h4, h5 {
  color: #FFFFFF;
  line-height: 1.4em;
  font-family: 'Playfair Display';
  font-style: italic;
  font-weight: 700;
}

h2 {
  font-size: 3em;
}

h3 {
  font-size: 1.5em;
}

a {
  text-decoration: none;
}

main > .header {
  order: 3;
  text-align: center;
}

.accessible-hide {
  position: absolute;
  overflow: hidden;
  height: 0;
  text-indent: -900em;
}

@-webkit-keyframes logoAnim {
  45%,
    55% {
    stroke-dashoffset: 10em;
  }
}

@keyframes logoAnim {
  45%,
    55% {
    stroke-dashoffset: 10em;
  }
}
.logo-tadaima {
  height: 3.75em;
}
.logo-tadaima--animated {
  stroke-dasharray: 10em .2em 10em .2em 10em .2em 10em;
  stroke-dashoffset: 0;
  -webkit-animation: logoAnim 9s cubic-bezier(0.54, -0.24, 0.46, 1.28) infinite;
          animation: logoAnim 9s cubic-bezier(0.54, -0.24, 0.46, 1.28) infinite;
}

.svg-bg {
  width: 100%;
  height: 100%;
  position: fixed;
  left: 0;
  top: 0;
  z-index: 1;
}

.svg-icon {
  width: 1em;
  height: 1em;
  transform-origin: 50% 50%;
}
.svg-icon__sprite {
  display: none;
}
.svg-icon--rotated-180 {
  transform: rotate(180deg);
}

.space--small {
  margin-bottom: 0.7em;
}
@media (max-width: 75em) {
  .space--small {
    margin-bottom: 0.518em;
  }
}

.space--normal {
  margin-bottom: 1.4em;
}
@media (max-width: 75em) {
  .space--normal {
    margin-bottom: 1.036em;
  }
}

.space--medium {
  margin-bottom: 2.8em;
}
@media (max-width: 75em) {
  .space--medium {
    margin-bottom: 2.072em;
  }
}

.space--big {
  margin-bottom: 4.2em;
}
@media (max-width: 75em) {
  .space--big {
    margin-bottom: 3.108em;
  }
}

.space--huge {
  margin-bottom: 5.6em;
}
@media (max-width: 75em) {
  .space--huge {
    margin-bottom: 4.144em;
  }
}

.color--white {
  color: #FFFFFF;
}

.fill--white {
  fill: #FFFFFF;
}

.stroke--white {
  stroke: #FFFFFF;
}

.color--black {
  color: #000000;
}

.fill--black {
  fill: #000000;
}

.stroke--black {
  stroke: #000000;
}

.color--red {
  color: #FF5572;
}

.fill--red {
  fill: #FF5572;
}

.stroke--red {
  stroke: #FF5572;
}

.color--coral {
  color: #FF6960;
}

.fill--coral {
  fill: #FF6960;
}

.stroke--coral {
  stroke: #FF6960;
}

.color--orange {
  color: #FF7555;
}

.fill--orange {
  fill: #FF7555;
}

.stroke--orange {
  stroke: #FF7555;
}

.color--gray {
  color: #404040;
}

.fill--gray {
  fill: #404040;
}

.stroke--gray {
  stroke: #404040;
}

.svg-icon {
  stroke-width: 3;
}

.video {
  width: 30em;
  position: relative;
  overflow: hidden;
  font-size: 1.2em;
  box-shadow: 0 2.5em 2.5em -1.875em rgba(0, 0, 0, 0.5), 0 1.25em 5em 1em rgba(0, 0, 0, 0.2);
}
.video__player {
  width: 100%;
  height: 100%;
  display: inline-block;
}
.video__control {
  width: 100%;
  bottom: 0;
  left: 0;
  z-index: 2;
  position: absolute;
  box-sizing: border-box;
  padding: 0 1em;
  background-color: rgba(0, 0, 0, 0.65);
  transition: all 0.3s ease-in-out;
}
@media (min-width: 65em) {
  .video__control {
    opacity: 0;
    transform: translate(0, 100%);
  }
}
.video__control__button {
  padding: 1em .5em;
  display: flex;
  cursor: pointer;
  position: relative;
  transition: all 0.3s ease-in-out;
}
.video__control__button:before {
  content: '';
  display: inline-block;
  width: 100%;
  height: 1.9em;
  z-index: -1;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%) scale(0);
  border-radius: 1.9em;
  background-color: #FF5572;
  transition: all 0.15s cubic-bezier(0.54, -0.24, 0.46, 1.28);
}
.video__control__button.volume {
  flex-basis: 2em;
}
.video__control__button:hover:before, .video__control__button.active:before {
  transform: translate(-50%, -50%) scale(1);
}
.video__control__button:hover > .video__track__range__sound, .video__control__button.active > .video__track__range__sound {
  padding-left: .5em;
  pointer-events: all;
  opacity: 1;
  flex: 1;
}
@media (-webkit-min-device-pixel-ratio: 2) {
  .video__control > .video__control__button.volume {
    display: none;
  }
}
.video__control > .video__control__button.volume:hover {
  flex-basis: 5em;
}
.video__duration {
  padding-right: .5em;
  font-size: .5em;
  color: rgba(255, 255, 255, 0.5);
}
.video__track__range[type=range] {
  -webkit-appearance: inherit;
  /* WebKit */
  width: 100%;
  background-color: transparent;
}
.video__track__range[type=range]:focus {
  outline: none;
}
.video__track__range[type=range]::-webkit-slider-runnable-track {
  width: 100%;
  height: 1.5em;
  box-sizing: border-box;
  cursor: pointer;
  box-shadow: none;
  background: transparent;
  border-radius: 1.5em;
  border: 2px solid #FFFFFF;
}
.video__track__range[type=range]::-webkit-slider-thumb {
  box-shadow: none;
  height: 1.5em;
  width: 1.5em;
  border-radius: 50%;
  box-sizing: border-box;
  border: 2px solid #FFFFFF;
  background: transparent;
  cursor: pointer;
  -webkit-appearance: none;
  margin-top: -2px;
}
.video__track__range[type=range]::-moz-range-track {
  width: 100%;
  height: 1.5em;
  box-sizing: border-box;
  cursor: pointer;
  box-shadow: none;
  background: transparent;
  border-radius: 1.5em;
  border: 2px solid #FFFFFF;
}
.video__track__range[type=range]::-moz-range-thumb {
  box-shadow: none;
  border: 0;
  height: 1.5em;
  width: 1.5em;
  border-radius: 50%;
  box-sizing: border-box;
  border: 2px solid #FFFFFF;
  background: transparent;
  cursor: pointer;
}
.video__track__range[type=range]::-ms-track {
  width: 100%;
  height: 1.5em;
  box-sizing: border-box;
  cursor: pointer;
  background: transparent;
  border-color: transparent;
  color: transparent;
  border: 2px solid #FFFFFF;
}
.video__track__range[type=range]::-ms-fill-lower {
  background: transparent;
  border: 0;
  border-radius: 1.5em;
  box-shadow: none;
}
.video__track__range[type=range]::-ms-fill-upper {
  background: transparent;
  border: 0;
  border-radius: 1.5em;
  box-shadow: none;
}
.video__track__range[type=range]::-ms-thumb {
  box-shadow: none;
  border: 0;
  height: 1.5em;
  width: 1.5em;
  border-radius: 50%;
  box-sizing: border-box;
  border: 2px solid #FFFFFF;
  background: transparent;
  cursor: pointer;
}
.video__track__range[type=range]:focus::-ms-fill-lower {
  background: transparent;
}
.video__track__range[type=range]:focus::-ms-fill-upper {
  background: transparent;
}
.video__track__range__sound {
  display: flex;
  width: 0;
  opacity: 0;
  padding-left: 0;
  pointer-events: none;
  transition: all 0.15s cubic-bezier(0.54, -0.24, 0.46, 1.28);
}
.video:hover .video__control {
  opacity: 1;
  transform: translate(0, 0);
}

.tooltip {
  position: relative;
}
.tooltip:after {
  content: attr(data-tooltip-content);
  position: absolute;
  bottom: 100%;
  left: 50%;
  transform: translate(-50%, 0);
  padding: 1em;
  font-size: 12px;
  color: #FFFFFF;
  background-color: #141414;
  opacity: 0;
  transition: all 0.3s cubic-bezier(0.54, -0.24, 0.46, 1.28);
}
.tooltip:hover:after {
  opacity: 1;
}
</style>