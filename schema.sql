-- Enable uuid-ossp for uuid_generate_v4()
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- ------------------------------------------------------------------------------
-- FUNCTION to handle automatic updated_at
-- ------------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION set_updated_at()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- ------------------------------------------------------------------------------
-- TABLES
-- ------------------------------------------------------------------------------

-- 1. users
CREATE TABLE IF NOT EXISTS users (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(), 
  firebase_uid VARCHAR(255) UNIQUE NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  display_name VARCHAR(255),
  created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(), 
  updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);

-- 2. rss_feeds
CREATE TABLE IF NOT EXISTS rss_feeds (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(), 
  feed_url TEXT UNIQUE NOT NULL,
  title VARCHAR(511) NOT NULL,
  description TEXT,
  link TEXT,
  image_url TEXT,
  last_fetched_at TIMESTAMP WITH TIME ZONE,
  last_fetched_status VARCHAR(50),
  error_details TEXT,
  created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(), 
  updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);

-- 3. user_subscriptions
CREATE TABLE IF NOT EXISTS user_subscriptions (
  user_id UUID REFERENCES users(id),
  feed_id UUID REFERENCES rss_feeds(id),
  subscribed_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(), 
  is_active BOOLEAN NOT NULL DEFAULT TRUE,
  PRIMARY KEY (user_id, feed_id)
);

-- 4. user_bookmarks
CREATE TABLE IF NOT EXISTS user_bookmarks (
  user_id UUID REFERENCES users(id),
  feed_id UUID REFERENCES rss_feeds(id),
  bookmarked_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(), 
  PRIMARY KEY (user_id, feed_id)
);

-- 5. blog_posts
CREATE TABLE IF NOT EXISTS blog_posts (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(), 
  feed_id UUID NOT NULL REFERENCES rss_feeds(id),
  guid TEXT UNIQUE NOT NULL,
  title TEXT NOT NULL,
  link TEXT NOT NULL,
  published_at TIMESTAMP WITH TIME ZONE NOT NULL,
  author VARCHAR(255),
  content_html TEXT NOT NULL,
  summary TEXT,
  image_url TEXT,
  created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(), 
  updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);

-- 6. categories
CREATE TABLE IF NOT EXISTS categories (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(), 
  name VARCHAR(255) UNIQUE NOT NULL,
  slug VARCHAR(255) UNIQUE NOT NULL,
  description TEXT
);

-- 7. feed_categories
CREATE TABLE IF NOT EXISTS feed_categories (
  feed_id UUID REFERENCES rss_feeds(id),
  category_id UUID REFERENCES categories(id),
  PRIMARY KEY (feed_id, category_id)
);

-- ------------------------------------------------------------------------------
-- TRIGGERS to handle automatic updated_at
-- ------------------------------------------------------------------------------

CREATE TRIGGER set_users_updated_at
BEFORE UPDATE ON users
FOR EACH ROW EXECUTE FUNCTION set_updated_at();

CREATE TRIGGER set_feeds_updated_at
BEFORE UPDATE ON rss_feeds
FOR EACH ROW EXECUTE FUNCTION set_updated_at();

CREATE TRIGGER set_blog_posts_updated_at
BEFORE UPDATE ON blog_posts
FOR EACH ROW EXECUTE FUNCTION set_updated_at();

-- SQL schema for the User model
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL
);
