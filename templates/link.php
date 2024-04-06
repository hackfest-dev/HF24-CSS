<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="stylelink.css">
    <title>Document</title>
</head>

<body>
    <?php

    $link = $_POST['link'];
    ?>
    <br>

    <?php

    $output = shell_exec("python questionx.py $link");
    $file_path = 'z.txt';

    // Open the file for reading
    $file_handle = fopen($file_path, 'r');
    $questans = array(
        array(),
        array(),
        array(),
        array(),
        array(),
    );
    $i = 0;
    $j = 0;

    if ($file_handle === false) {
        // Error handling if the file could not be opened
        echo "Failed to open the file.";
    } else {
        // Read the file line by line
        while (($line = fgets($file_handle)) !== false) {
            $questans[$i][$j] = $line;
            $j = $j + 1;
            if ($j == 7) {
                $i = $i + 1;
                $j = 0;
            }
        }

        // Close the file handle
        fclose($file_handle);
    }

    ?>

    <div class="container">
        <header class="header">
            <h1 id="title" class="header__title">Generating quiz</h1>
            <p id="description" class="header__description">
                Generating questions based on your video link.
            </p>
            <img src="https://res.cloudinary.com/alexandracaulea/image/upload/v1585333913/illustration_x46ict.svg"
                alt="" aria-hidden="true" class="illustration" />
        </header>
        <main class="main">
            <form action="ans.php" method="post" id="survey-form" class="survey" novalidate>

                <section class="survey__panel survey__panel--current" aria-hidden="false" data-index="1"
                    data-panel="firstPanel" data-requirement="option">
                    <h2 class="survey__panel__question">
                        <span class="visuallyhidden">Question 1 </span>
                        <?php echo $questans[0][0]; ?>
                    </h2>
                    <div class="survey__panel__period">
                        <div class="form-group">
                            <input id="never" type="radio" name="question_1" value="<?php echo $questans[0][1]; ?>" />
                            <label for="never">
                                <?php echo $questans[0][1]; ?>
                            </label>
                        </div>
                        <div class="form-group">
                            <input id="lessthenoneyear" type="radio" name="question_1"
                                value="<?php echo $questans[0][2]; ?>" />
                            <label for="lessthenoneyear">
                                <?php echo $questans[0][2]; ?>
                            </label>
                        </div>
                        <div class="form-group">
                            <input id="onetotwoyears" type="radio" name="question_1"
                                value="<?php echo $questans[0][3]; ?>" />
                            <label for="onetotwoyears">
                                <?php echo $questans[0][3]; ?>
                            </label>
                        </div>
                        <div class="form-group">
                            <input id="morethentwoyears" type="radio" name="question_1"
                                value="<?php echo $questans[0][4]; ?>" />
                            <label for="morethentwoyears"><span class="visuallyhidden">more then</span>
                                <?php echo $questans[0][4]; ?>
                            </label>
                        </div>
                    </div>
                    <p class="error-message"></p>
                </section>


                <!--
                <section class="survey__panel" aria-hidden="true" data-index="3" data-panel="thirdPanel"
                    data-requirement="checkbox">
                    <h2 class="survey__panel__question">
                        <span class="visuallyhidden">Question 1 of 5 </span>
                        <?php echo $questans[2][0]; ?>
                    </h2>
                    <div class="survey__panel__period">
                        <div class="form-group">
                            <input id="never" type="radio" name="question_3" value="<?php echo $questans[2][1]; ?>" />
                            <label for="never">
                                <?php echo $questans[2][1]; ?>
                            </label>
                        </div>
                        <div class="form-group">
                            <input id="lessthenoneyear" type="radio" name="question_3"
                                value="<?php echo $questans[2][2]; ?>" />
                            <label for="lessthenoneyear">
                                <?php echo $questans[2][2]; ?>
                            </label>
                        </div>
                        <div class="form-group">
                            <input id="onetotwoyears" type="radio" name="question_3"
                                value="<?php echo $questans[2][3]; ?>" />
                            <label for="onetotwoyears">
                                <?php echo $questans[2][3]; ?>
                            </label>
                        </div>
                        <div class="form-group">
                            <input id="morethentwoyears" type="radio" name="question_3"
                                value="<?php echo $questans[2][4]; ?>" />
                            <label for="morethentwoyears"><span class="visuallyhidden">more then</span>
                                <?php echo $questans[2][4]; ?>
                            </label>
                        </div>
                    </div>
                    <p class="error-message"></p>
                </section>

                <section class="survey__panel" aria-hidden="true" data-index="4" data-panel="fourthPanel"
                    data-requirement="option">
                    <h2 class="survey__panel__question">
                        <span class="visuallyhidden">Question 1 of 5 </span>
                        <?php echo $questans[3][0]; ?>
                    </h2>
                    <div class="survey__panel__period">
                        <div class="form-group">
                            <input id="never" type="radio" name="question_4" value="<?php echo $questans[3][1]; ?>" />
                            <label for="never">
                                <?php echo $questans[3][1]; ?>
                            </label>
                        </div>
                        <div class="form-group">
                            <input id="lessthenoneyear" type="radio" name="question_4"
                                value="<?php echo $questans[3][2]; ?>" />
                            <label for="lessthenoneyear">
                                <?php echo $questans[3][2]; ?>
                            </label>
                        </div>
                        <div class="form-group">
                            <input id="onetotwoyears" type="radio" name="question_4"
                                value="<?php echo $questans[3][3]; ?>" />
                            <label for="onetotwoyears">
                                <?php echo $questans[3][3]; ?>
                            </label>
                        </div>
                        <div class="form-group">
                            <input id="morethentwoyears" type="radio" name="question_4"
                                value="<?php echo $questans[3][4]; ?>" />
                            <label for="morethentwoyears"><span class="visuallyhidden">more then</span>
                                <?php echo $questans[3][4]; ?>
                            </label>
                        </div>
                    </div>
                    <p class="error-message"></p>
                </section>

                <section class="survey__panel" aria-hidden="true" data-index="5" data-panel="fifthPanel"
                    data-requirement="name;email;country;age">
                    <h2 class="survey__panel__question">
                        <span class="visuallyhidden">Question 1 of 5 </span>
                        <?php echo $questans[4][0]; ?>
                    </h2>
                    <div class="survey__panel__period">
                        <div class="form-group">
                            <input id="never" type="radio" name="question_5" value="<?php echo $questans[4][1]; ?>" />
                            <label for="never">
                                <?php echo $questans[4][1]; ?>
                            </label>
                        </div>
                        <div class="form-group">
                            <input id="lessthenoneyear" type="radio" name="question_5"
                                value="<?php echo $questans[4][2]; ?>" />
                            <label for="lessthenoneyear">
                                <?php echo $questans[4][2]; ?>
                            </label>
                        </div>
                        <div class="form-group">
                            <input id="onetotwoyears" type="radio" name="question_5"
                                value="<?php echo $questans[4][3]; ?>" />
                            <label for="onetotwoyears">
                                <?php echo $questans[4][3]; ?>
                            </label>
                        </div>
                        <div class="form-group">
                            <input id="morethentwoyears" type="radio" name="question_5"
                                value="<?php echo $questans[4][4]; ?>" />
                            <label for="morethentwoyears"><span class="visuallyhidden">more then</span>
                                <?php echo $questans[4][4]; ?>
                            </label>
                        </div>
                    </div>
                    <p class="error-message"></p>
                </section>

-->
                <div class="form-buttons"><!--
                    <button class="button" type="button" name="prev" disabled="disabled" aria-label="Previous"
                        aria-hidden="true">
                        Prev
                    </button>
                    <button class="button" type="button" name="next" aria-label="Next" aria-hidden="false">Next</button>
                    <button class="button" type="submit" id="submit" name="submit" disabled="disabled"
                        aria-hidden="true">
                        Submit
                    </button>
-->
                    <button class="button" type="submit" name="next" id="submit" aria-label="Next"
                        aria-hidden="false">Submit</button>

                </div>
            </form>
        </main>
    </div>

    <script src="link.js"></script>
    <script>window.onfocus = function () {
            window.location.href = "./link.html";
        }</script>
</body>

</html>