-- Challenge 1

SELECT 
    au.au_id as "Author ID", au.au_fname as "FIRST NAME", au.au_lname as "LAST NAME", t.title as "TITLE" , pub.pub_name as "PUBLISHER"
	FROM authors AS au
	LEFT JOIN titleauthor AS ta ON ta.au_id=au.au_id 
	LEFT JOIN titles AS t ON t.title_id = ta.title_id
    LEFT JOIN publishers AS pub ON t.pub_id = pub.pub_id;
    
-- Challenge 2

SELECT 
    au.au_id as "Author ID", au.au_fname as "FIRST NAME", au.au_lname as "LAST NAME" , pub.pub_name as "PUBLISHER", count(*) as "TITLE COUNT"
	FROM authors AS au
	LEFT JOIN titleauthor AS ta ON ta.au_id=au.au_id 
	LEFT JOIN titles AS t ON t.title_id = ta.title_id
    LEFT JOIN publishers AS pub ON t.pub_id = pub.pub_id
    GROUP BY au.au_id, au.au_lname, au.au_fname, pub.pub_name
    ORDER BY "TITLE COUNT" DESC ;
    
-- Challenge 3 

SELECT 
    au.au_id as "Author ID", au.au_fname as "FIRST NAME", au.au_lname as "LAST NAME" , sum(t.ytd_sales) as "TOTAL"
	FROM authors AS au
	LEFT JOIN titleauthor AS ta ON ta.au_id=au.au_id 
	LEFT JOIN titles AS t ON t.title_id = ta.title_id
    GROUP BY au.au_id, au.au_lname, au.au_fname
    ORDER BY sum(t.ytd_sales) DESC LIMIT 3;
    
-- Challenge 4 

SELECT 
    au.au_id as "Author ID", au.au_fname as "FIRST NAME", au.au_lname as "LAST NAME" , sum(t.ytd_sales) as "TOTAL"
	FROM authors AS au
	LEFT JOIN titleauthor AS ta ON ta.au_id=au.au_id 
	LEFT JOIN titles AS t ON t.title_id = ta.title_id
    GROUP BY au.au_id, au.au_lname, au.au_fname
    ORDER BY sum(t.ytd_sales) DESC ;
    
-- Bonus
-- No lo he conseguido. 
