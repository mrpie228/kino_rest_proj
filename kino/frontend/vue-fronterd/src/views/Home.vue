<template>

<section class="main-container" >
      <div class="location" id="home">
          <h1 id="home">Рекомендуем:</h1>
          <div   class="box">
            <a v-for="movie in movies" v-bind:key="movie.id" ><img :src="movie.poster" alt="" @click="goTo(movie.url)" ><br></a>
          </div>
          <h1 id="tvShows">TV Шоу:</h1>
      <div class="box">
        <a><img src="https://github.com/carlosavilae/Netflix-Clone/blob/master/img/tv1.PNG?raw=true" alt=""></a>
        <a href=""><img src="https://github.com/carlosavilae/Netflix-Clone/blob/master/img/tv2.PNG?raw=true" alt=""></a>
        <a href=""><img src="https://github.com/carlosavilae/Netflix-Clone/blob/master/img/tv3.PNG?raw=true" alt=""></a>
        <a href=""><img src="https://github.com/carlosavilae/Netflix-Clone/blob/master/img/tv4.PNG?raw=true" alt=""></a>
        <a href=""><img src="https://github.com/carlosavilae/Netflix-Clone/blob/master/img/tv5.PNG?raw=true" alt=""></a>
        <a href=""><img src="https://github.com/carlosavilae/Netflix-Clone/blob/master/img/tv6.PNG?raw=true" alt=""></a>

        <a href=""><img src="https://github.com/carlosavilae/Netflix-Clone/blob/master/img/tv7.PNG?raw=true" alt=""></a>
        <a href=""><img src="https://github.com/carlosavilae/Netflix-Clone/blob/master/img/tv8.PNG?raw=true" alt=""></a>
        <a href=""><img src="https://github.com/carlosavilae/Netflix-Clone/blob/master/img/tv9.PNG?raw=true" alt=""></a>
        <a href=""><img src="https://github.com/carlosavilae/Netflix-Clone/blob/master/img/tv10.PNG?raw=true" alt=""></a>
        <a href=""><img src="https://github.com/carlosavilae/Netflix-Clone/blob/master/img/tv11.PNG?raw=true" alt=""></a>
        <a href=""><img src="https://github.com/carlosavilae/Netflix-Clone/blob/master/img/tv12.PNG?raw=true" alt=""></a>              
      </div>
      </div>
</section>

</template>


<script>
// @ is an alias to /src
//import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  components: {
  },
  data(){
    return{
      movies:[],
    }
  },
    created() {
      this.loadMovies()
    },
  methods: {
    async loadMovies(){
      this.movies = await fetch(
        `http://127.0.0.1:8000/api/v2/movie/`
      ).then(response=>response.json())
    },
 
    goTo(url){
      this.$router.push({name:"OneMovie", params: {url:url} })
    }
   },
  }

</script>
