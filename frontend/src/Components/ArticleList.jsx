import React, { Component } from 'react';
import ArticleService from './ArticleService'

const articleService = new ArticleService();

class ArticleList extends Component {

  constructor(props) {
    super(props);
    this.state = {
      articles: [],
      nextPageURL: ''
    };
    this.nextPage = this.nextPage.bind(this);
    this.handleDelete = this.handleDelete.bind(this);
  }

  componentDidMount () {
    var self = this;
    articleService.getArticles().then(function (result) {
      self.setState({articles: result.data, nextPageURL: result.nextlink})
    })
  }

  handleDelete(e,pk){
    var self = this;
    articleService.deleteArticle({pk: pk}).then(()=>{
      var newArr = self.state.articles.filter(function(obj){
        return obj.pk !== pk;
      });
      self.setState({articles: newArr})
    });
  }

  nextPage(){
    var self = this;
    articleService.getArticlesByURL(self.state.nextPageURL).then((result) => {
      self.setState({ articles: result.data, nextPageURL: result.nextlink})
    });
  }

  render() {
    return (
      <div className="newscontainer">
        <div id="tlmnews">
          <h1 id="newsHeader">The last manifesto news</h1>
        </div>
        <div id ="globalnews">
          <h1 id="newsHeader">Global News</h1>
          {this.state.articles.map( c  =>
            <div>
              {c.pk}
              {c.headline}
              {c.trailtext}
              {c.thumbnail}
              {c.url}
              {c.source}
            <button  onClick={(e)=>  this.handleDelete(e,c.pk) }> Delete</button>
            <a  href={"/article/" + c.pk}> Update</a>
            </div>
            )}

          <button  className="btn btn-primary"  onClick=  {  this.nextPage  }>Next</button>
        </div>
      </div>
      );
    }
  }

export default ArticleList;
