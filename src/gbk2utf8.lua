-- iconv -f gbk -t utf-8 "$1" -o "build/$1"

local lfs = require "lfs"

local inputDir, outputDir = ...

-- 递归遍历 inputDir, 对每个文件执行 func
local function traverse(dir, func)
	for file in lfs.dir(dir) do
		if file ~= "." and file ~= ".." then
			local path = dir .. "/" .. file
			local attr = lfs.attributes(path)
			assert(type(attr) == "table")
			if attr.mode == "directory" then
				traverse(path)
			else
				func(path)
			end
		end
	end
end

traverse(inputDir, function(path)
	local cmd = string.format([[iconv -f gbk -t utf-8 "%s" -o "%s/%s"]], path, outputDir, file)
	print(cmd)
	os.execute(cmd)
end)
