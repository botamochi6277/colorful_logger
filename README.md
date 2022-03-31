# colorful logger

Python package to logging with colorful text.

```bash
pip install git+https://github.com/botamochi6277/colorful_logger.git@main
```

```python
import colorful_logger
if __name__ == '__main__':
    logger = get_colorful_logger()
    logger.debug('hello debug')
    logger.info('hello info')
    logger.warning('hello warning')
    logger.error('hello error')
    logger.critical('hello critical')
```

<img width="369" alt="ScreenShot 2022-03-31 23 51 42" src="https://user-images.githubusercontent.com/14128408/161085283-3c8aec68-abea-4057-9202-a8ae3ac3c50b.png">
