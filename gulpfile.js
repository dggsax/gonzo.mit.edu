var less = require('gulp-less');
var gulp = require('gulp');
var path = require('path');

gulp.task('default', function() {
    // place code for your default task here
});

// stuff to compile less file to css for website
gulp.task('less', function () {
    return gulp.src('static/less/*.less')
        .pipe(less({
            paths: [ path.join(__dirname, 'less', 'includes') ]
        }))
        .pipe(gulp.dest('static/css'));
});