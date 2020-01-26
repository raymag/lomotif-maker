############## The Movie Maker ##############
############# Coded by: Raymag ##############
#############################################
import os
import click

@click.group()
def mmk():
    pass

@mmk.command()
@click.argument('path', type=click.Path(exists=True))
def rename(path):
    ''' Rename all jpg files in a given path '''

    path_divisor = ''
    if '//' in path:
        path_divisor = '//'
    if '/' in path:
        path_divisor = '/'
    if '\\' in path:
        path_divisor = '\\'
    
    length = len(path_divisor)
    if path[-length::] != path_divisor:
        path+=path_divisor

    save_directory = 'mmk_pics_{}'
    i = 1
    click.echo(path+save_directory.format(i))
    while os.path.isdir(path+save_directory.format(i)):
        i+=1
    save_directory = save_directory.format(i)

    click.echo('Creating new directory: '+path+save_directory)
    os.mkdir(path+save_directory)

    click.echo('Renaming all images in '+path)
    i = 1
    destiny = path+save_directory+path_divisor
    for filename in os.listdir(path):
        f_extension = filename.split('.')[-1]
        if f_extension == 'jpg':
            new_filename = 'img_'+str(i)+'.jpg'
            click.echo('Renaming ['+filename+'] to ['+destiny+new_filename+']')
            os.rename(path+filename, '{}{}'.format(destiny, new_filename))
            i+=1
    i -= 1
    if i == 1:
        click.echo('{} file was successfully renamed and moved to {}.'.format(str(i), destiny))
    else:
        click.echo('{} files were successfully renamed and moved to {}.'.format(str(i), destiny))
    click.echo('Done.')

@mmk.command()
@click.argument('img_path', type=click.Path(exists=True))
@click.argument('audio_path', type=click.Path(exists=True))
def make_movie(img_path, audio_path):
    ''' Merges all organized jpg images into a avi video with a given soundtrack '''

    path_divisor = ''
    if '//' in img_path:
        path_divisor = '//'
    if '/' in img_path:
        path_divisor = '/'
    if '\\' in img_path:
        path_divisor = '\\'
    
    length = len(path_divisor)
    if img_path[-length::] != path_divisor:
        img_path+=path_divisor

    save_directory = 'mmk_movie_{}'
    i = 1
    while os.path.isdir(img_path+save_directory.format(i)):
        i+=1
    save_directory = save_directory.format(i)

    click.echo('Creating new directory: '+img_path+save_directory)
    os.mkdir(img_path+save_directory)
    destiny = img_path+save_directory+path_divisor

    click.echo('Making the movie.')
    img_total = 0
    for filename in os.listdir(img_path):
        f = filename.split('.')
        if f[-1] == 'jpg':
            img_total+=1
    os.system('ffmpeg -f image2 -r 4/5 -i {} -vcodec mjpeg -b 5000 -q:v 1 -y {}'.format(img_path+'img_%01d.jpg', destiny+'mute.avi'))
    click.echo('{} images was turned into one movie in [{}].'.format(img_total, destiny))

    try:
        os.system('ffmpeg -i {} -i "{}" -codec copy -shortest {}'.format(destiny+'mute.avi', audio_path, destiny+'movie.avi'))
        os.remove(destiny+'mute.avi')
    except:
        pass

    click.echo("Done.")

if __name__ == '__main__':
    mmk()