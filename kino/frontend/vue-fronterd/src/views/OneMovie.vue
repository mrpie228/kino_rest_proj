<template>

<section class="main-container" >
  
     <div class="location" id="one_film">
          <h1 id="home">{{movie.title}}</h1>
          <h4 id="desription">{{movie.description}}</h4>
          <h4 id="year">{{movie.year}}</h4>
          <h4 id="star">{{movie.star}}</h4>
          <h4 id="star">{{movie.fees_in_world}}</h4>
          <div   class="box">
            <a ><img :src="movie.poster" alt="" ><br></a>
          </div>
      </div>

</section>

  <!--<div v-for="movie in movies" v-bind:key="movie.id">
  <a>{{movie.title}}</a>
  <a> {{movie.middle_rating}}</a>
  <a> {{movie.that_user_rating}}</a>
  </div>
  </div>-->

</template>


<script>
// @ is an alias to /src
//import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'OneMovie',
  props:['url'],
  data(){
    return{
      movie:{},
 
    }
  },
  created() {
      this.loadMovie()
    },
  methods: {
    async loadMovie(){
      this.movie = await fetch(
        `http://127.0.0.1:8000/api/v2/movie/${this.url}/`
      ).then(response=>response.json()).then(console.log(this.movie))
    }
  }
}

</script>
