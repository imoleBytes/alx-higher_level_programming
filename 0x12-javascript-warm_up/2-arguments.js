#!/usr/bin/node

let lenght_of_argv = process.argv.length

if (lenght_of_argv < 3)
{
	console.log('No argument');
}
else if (lenght_of_argv === 3)
{
	console.log('Argument found');
}
else
{
	console.log('Arguments found');
}
