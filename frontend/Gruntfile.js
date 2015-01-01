/*!
 * Toraysoft's Gruntfile
 * http://www.toraysoft.com/
 * © Copyright 2011. Toraysoft All Rights Reserved
 */

module.exports = function(grunt) {

  // 相关的grunt插件的配置
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    
    //
    // less和css相关插件
    //=========================================
    
    // less编译插件
    less: {
      options: {
        strictMath: true,
        sourceMap: true,
        outputSourceFiles: true,
        sourceMapURL: '<%= pkg.name %>.css.map',
        sourceMapFilename: 'css/<%= pkg.name %>.css.map'
      },
      dist: {
        src: [
            'less/<%= pkg.name %>.base.less'
        ],
        dest: 'css/<%= pkg.name %>.css'
      }
    },
    
    // css代码检查插件
    csslint: {
      src: [
        '<%= less.dist.dest %>'
      ]
    },
    
    // css压缩插件
    cssmin: {
      options: {
        compatibility: 'ie8',
        keepSpecialComments: '*',
        noAdvanced: true
      },
      core: {
        files: {
          'css/<%= pkg.name %>.min.css': '<%= less.dist.dest %>'
        }
      }
    },
    
    //
    // js相关插件
    //=========================================
    
    // JSHint代码检查插件
    jshint: {
      files: ['Gruntfile.js', 'js/*.js'],
      options: {
        // 这里是覆盖JSHint默认配置的选项
        globals: {
          jQuery: true,
          console: true,
          module: true,
          document: true
        }
      }
    },
    
    // js合并插件
    concat: {
      options: {
        separator: ';'
      },
      dist: {
        src: [
            'js/ts.class.js',
            'js/**/*.js'
        ],
        dest: 'js/<%= pkg.name %>.js'
      }
    },
    
    // js压缩插件
    uglify: {
      options: {
        banner: '/*! <%= pkg.name %> <%= grunt.template.today("dd-mm-yyyy") %> */\n'
      },
      dist: {
        files: {
          'js/<%= pkg.name %>.min.js': ['<%= concat.dist.dest %>']
        }
      }
    },
    
    
    //
    // 其他grunt插件
    //=========================================
    
    // 清理生成的css和js文件
    clean: {
      js: ['js/<%= pkg.name %>.js', 'js/<%= pkg.name %>.min.js'],
      css: ['css']
    },
    
    // 检测文件发生变化时，执行合并任务
    watch: {
      less: {
        files: 'less/*.less',
        tasks: 'less'
      }
    }
    
  });

  //
  // 加载package.json中devDependencies定义的grunt插件包
  require('load-grunt-tasks')(grunt, { scope: 'devDependencies' });

  //
  // 创建测试任务
  grunt.registerTask('test', ['jshint', 'csslint']);

  //
  // 创建js合并压缩任务
  grunt.registerTask('core-js', ['clean:js', 'concat', 'uglify']);
  
  //
  // 创建js合并压缩任务
  grunt.registerTask('core-css', ['clean:css', 'less', 'cssmin']);
  
  //
  // 定义默认情况下的任务
  grunt.registerTask('default', ['core-css']);
  

};