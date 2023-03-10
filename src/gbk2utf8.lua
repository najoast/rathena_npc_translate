-- #/bin/sh

-- # first argument is the folder to search
-- # second argument is output folder

-- SEARCH_FOLDER=$1
-- OUTPUT_FOLDER=$2

-- for f in $SEARCH_FOLDER
-- do
--     if [ -d "$f" ]; then
--         for ff in $f/*
-- 		do
--             echo "Processing $ff"
-- 			iconv -f gbk -t utf-8 "$ff" -o "${OUTPUT_FOLDER}${ff}"
--         done
--     fi
-- done
