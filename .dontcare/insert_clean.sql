
CREATE TABLE IF NOT EXISTS sio
(
    User varchar(50), 
    Restaurant1 FLOAT,
    Restaurant2 FLOAT,
    Restaurant3 FLOAT,
    Restaurant4 FLOAT,
    Restaurant5 FLOAT,
    Restaurant6 FLOAT,
    Restaurant7 FLOAT,
    Restaurant8 FLOAT,
    Restaurant9 FLOAT,
    Restaurant10 FLOaT,
    Restaurant11 FLOAT,
    Restaurant12 FLOAT,
    Restaurant13 FLOAT,
    Restaurant14 FLOAT,
    Restaurant15 FLOAT,
    Restaurant16 FLOAT,
    Restaurant17 FLOAT,
    Restaurant18 FLOAT,
    Restaurant19 FLOAT,
    Restaurant20 FLOAT,
    Restaurant21 FLOAT,
    Restaurant22 FLOAT,
    Restaurant23 FLOAT,
    Restaurant24 FLOAT,
    Restaurant25 FLOAT,
    Restaurant26 FLOAT,
    Restaurant27 FLOAT,
    Restaurant28 FLOAT,
    Restaurant29 FLOAT,
    Restaurant30 FLOAT,
    Restaurant31 FLOAT,
    Restaurant32 FLOAT,
    Restaurant33 FLOAT,
    Restaurant34 FLOAT,
    Restaurant35 FLOAT,
    Restaurant36 FLOAT,
    Restaurant37 FLOAT,
    Restaurant38 FLOAT,
    Restaurant39 FLOAT,
    Restaurant40 FLOAT,
    Restaurant41 FLOAT,
    Restaurant42 FLOAT,
    Restaurant43 FLOAT,
    Restaurant44 FLOAT,
    Restaurant45 FLOAT,
    Restaurant46 FLOAT,
    Restaurant47 FLOAT,
    Restaurant48 FLOAT,
    Restaurant49 FLOAT,
    Restaurant50 FLOAT,
    Restaurant51 FLOAT,
    Restaurant52 FLOAT,
    Restaurant53 FLOAT,
    Restaurant54 FLOAT,
    Restaurant55 FLOAT,
    Restaurant56 FLOAT,
    Restaurant57 FLOAT,
    Restaurant58 FLOAT,
    Restaurant59 FLOAT,
    Restaurant60 FLOAT,
    Restaurant61 FLOAT,
    Restaurant62 FLOAT,
    Restaurant63 FLOAT,
    Restaurant64 FLOAT,
    Restaurant65 FLOAT,
    Restaurant66 FLOAT,
    Restaurant67 FLOAT,
    Restaurant68 FLOAT,
    Restaurant69 FLOAT,
    Restaurant70 FLOAT,
    Restaurant71 FLOAT,
    Restaurant72 FLOAT,
    Restaurant73 FLOAT,
    Restaurant74 FLOAT,
    Restaurant75 FLOAT,
    Restaurant76 FLOAT,
    Restaurant77 FLOAT,
    Restaurant78 FLOAT,
    Restaurant79 FLOAT,
    Restaurant80 FLOAT,
    Restaurant81 FLOAT,
    Restaurant82 FLOAT,
    Restaurant83 FLOAT,
    Restaurant84 FLOAT,
    Restaurant85 FLOAT,
    Restaurant86 FLOAT,
    Restaurant87 FLOAT,
    Restaurant88 FLOAT,
    Restaurant89 FLOAT,
    Restaurant90 FLOAT,
    Restaurant91 FLOAT,
    Restaurant92 FLOAT,
    Restaurant93 FLOAT,
    Restaurant94 FLOAT,
    Restaurant95 FLOAT,
    Restaurant96 FLOAT,
    Restaurant97 FLOAT,
    Restaurant98 FLOAT,
    Restaurant99 FLOAT,
    Restaurant100 FLOAT,
    PRIMARY KEY (User)
) ENGINE InnoDB;
LOAD DATA INFILE '/var/lib/mysql-files/datasetUNIX.csv' INTO TABLE SIO.dataset FIELDS TERMINATED BY ';';
UPDATE SIO.dataset SET Restaurant1 = null where Restaurant1 = 99;
UPDATE SIO.dataset SET Restaurant2 = null where Restaurant2 = 99;
UPDATE SIO.dataset SET Restaurant3 = null where Restaurant3 = 99;
UPDATE SIO.dataset SET Restaurant4 = null where Restaurant4 = 99;
UPDATE SIO.dataset SET Restaurant5 = null where Restaurant5 = 99;
UPDATE SIO.dataset SET Restaurant6 = null where Restaurant6 = 99;
UPDATE SIO.dataset SET Restaurant7 = null where Restaurant7 = 99;
UPDATE SIO.dataset SET Restaurant8 = null where Restaurant8 = 99;
UPDATE SIO.dataset SET Restaurant9 = null where Restaurant9 = 99;
UPDATE SIO.dataset SET Restaurant10 = null where Restaurant10 = 99;
UPDATE SIO.dataset SET Restaurant11 = null where Restaurant11 = 99;
UPDATE SIO.dataset SET Restaurant12 = null where Restaurant12 = 99;
UPDATE SIO.dataset SET Restaurant13 = null where Restaurant13 = 99;
UPDATE SIO.dataset SET Restaurant14 = null where Restaurant14 = 99;
UPDATE SIO.dataset SET Restaurant15 = null where Restaurant15 = 99;
UPDATE SIO.dataset SET Restaurant16 = null where Restaurant16 = 99;
UPDATE SIO.dataset SET Restaurant17 = null where Restaurant17 = 99;
UPDATE SIO.dataset SET Restaurant18 = null where Restaurant18 = 99;
UPDATE SIO.dataset SET Restaurant19 = null where Restaurant19 = 99;
UPDATE SIO.dataset SET Restaurant20 = null where Restaurant20 = 99;
UPDATE SIO.dataset SET Restaurant21 = null where Restaurant21 = 99;
UPDATE SIO.dataset SET Restaurant22 = null where Restaurant22 = 99;
UPDATE SIO.dataset SET Restaurant23 = null where Restaurant23 = 99;
UPDATE SIO.dataset SET Restaurant24 = null where Restaurant24 = 99;
UPDATE SIO.dataset SET Restaurant25 = null where Restaurant25 = 99;
UPDATE SIO.dataset SET Restaurant26 = null where Restaurant26 = 99;
UPDATE SIO.dataset SET Restaurant27 = null where Restaurant27 = 99;
UPDATE SIO.dataset SET Restaurant28 = null where Restaurant28 = 99;
UPDATE SIO.dataset SET Restaurant29 = null where Restaurant29 = 99;
UPDATE SIO.dataset SET Restaurant30 = null where Restaurant30 = 99;
UPDATE SIO.dataset SET Restaurant31 = null where Restaurant31 = 99;
UPDATE SIO.dataset SET Restaurant32 = null where Restaurant32 = 99;
UPDATE SIO.dataset SET Restaurant33 = null where Restaurant33 = 99;
UPDATE SIO.dataset SET Restaurant34 = null where Restaurant34 = 99;
UPDATE SIO.dataset SET Restaurant35 = null where Restaurant35 = 99;
UPDATE SIO.dataset SET Restaurant36 = null where Restaurant36 = 99;
UPDATE SIO.dataset SET Restaurant37 = null where Restaurant37 = 99;
UPDATE SIO.dataset SET Restaurant38 = null where Restaurant38 = 99;
UPDATE SIO.dataset SET Restaurant39 = null where Restaurant39 = 99;
UPDATE SIO.dataset SET Restaurant40 = null where Restaurant40 = 99;
UPDATE SIO.dataset SET Restaurant41 = null where Restaurant41 = 99;
UPDATE SIO.dataset SET Restaurant42 = null where Restaurant42 = 99;
UPDATE SIO.dataset SET Restaurant43 = null where Restaurant43 = 99;
UPDATE SIO.dataset SET Restaurant44 = null where Restaurant44 = 99;
UPDATE SIO.dataset SET Restaurant45 = null where Restaurant45 = 99;
UPDATE SIO.dataset SET Restaurant46 = null where Restaurant46 = 99;
UPDATE SIO.dataset SET Restaurant47 = null where Restaurant47 = 99;
UPDATE SIO.dataset SET Restaurant48 = null where Restaurant48 = 99;
UPDATE SIO.dataset SET Restaurant49 = null where Restaurant49 = 99;
UPDATE SIO.dataset SET Restaurant50 = null where Restaurant50 = 99;
UPDATE SIO.dataset SET Restaurant51 = null where Restaurant51 = 99;
UPDATE SIO.dataset SET Restaurant52 = null where Restaurant52 = 99;
UPDATE SIO.dataset SET Restaurant53 = null where Restaurant53 = 99;
UPDATE SIO.dataset SET Restaurant54 = null where Restaurant54 = 99;
UPDATE SIO.dataset SET Restaurant55 = null where Restaurant55 = 99;
UPDATE SIO.dataset SET Restaurant56 = null where Restaurant56 = 99;
UPDATE SIO.dataset SET Restaurant57 = null where Restaurant57 = 99;
UPDATE SIO.dataset SET Restaurant58 = null where Restaurant58 = 99;
UPDATE SIO.dataset SET Restaurant59 = null where Restaurant59 = 99;
UPDATE SIO.dataset SET Restaurant60 = null where Restaurant60 = 99;
UPDATE SIO.dataset SET Restaurant61 = null where Restaurant61 = 99;
UPDATE SIO.dataset SET Restaurant62 = null where Restaurant62 = 99;
UPDATE SIO.dataset SET Restaurant63 = null where Restaurant63 = 99;
UPDATE SIO.dataset SET Restaurant64 = null where Restaurant64 = 99;
UPDATE SIO.dataset SET Restaurant65 = null where Restaurant65 = 99;
UPDATE SIO.dataset SET Restaurant66 = null where Restaurant66 = 99;
UPDATE SIO.dataset SET Restaurant67 = null where Restaurant67 = 99;
UPDATE SIO.dataset SET Restaurant68 = null where Restaurant68 = 99;
UPDATE SIO.dataset SET Restaurant69 = null where Restaurant69 = 99;
UPDATE SIO.dataset SET Restaurant70 = null where Restaurant70 = 99;
UPDATE SIO.dataset SET Restaurant71 = null where Restaurant71 = 99;
UPDATE SIO.dataset SET Restaurant72 = null where Restaurant72 = 99;
UPDATE SIO.dataset SET Restaurant73 = null where Restaurant73 = 99;
UPDATE SIO.dataset SET Restaurant74 = null where Restaurant74 = 99;
UPDATE SIO.dataset SET Restaurant75 = null where Restaurant75 = 99;
UPDATE SIO.dataset SET Restaurant76 = null where Restaurant76 = 99;
UPDATE SIO.dataset SET Restaurant77 = null where Restaurant77 = 99;
UPDATE SIO.dataset SET Restaurant78 = null where Restaurant78 = 99;
UPDATE SIO.dataset SET Restaurant79 = null where Restaurant79 = 99;
UPDATE SIO.dataset SET Restaurant80 = null where Restaurant80 = 99;
UPDATE SIO.dataset SET Restaurant81 = null where Restaurant81 = 99;
UPDATE SIO.dataset SET Restaurant82 = null where Restaurant82 = 99;
UPDATE SIO.dataset SET Restaurant83 = null where Restaurant83 = 99;
UPDATE SIO.dataset SET Restaurant84 = null where Restaurant84 = 99;
UPDATE SIO.dataset SET Restaurant85 = null where Restaurant85 = 99;
UPDATE SIO.dataset SET Restaurant86 = null where Restaurant86 = 99;
UPDATE SIO.dataset SET Restaurant87 = null where Restaurant87 = 99;
UPDATE SIO.dataset SET Restaurant88 = null where Restaurant88 = 99;
UPDATE SIO.dataset SET Restaurant89 = null where Restaurant89 = 99;
UPDATE SIO.dataset SET Restaurant90 = null where Restaurant90 = 99;
UPDATE SIO.dataset SET Restaurant91 = null where Restaurant91 = 99;
UPDATE SIO.dataset SET Restaurant92 = null where Restaurant92 = 99;
UPDATE SIO.dataset SET Restaurant93 = null where Restaurant93 = 99;
UPDATE SIO.dataset SET Restaurant94 = null where Restaurant94 = 99;
UPDATE SIO.dataset SET Restaurant95 = null where Restaurant95 = 99;
UPDATE SIO.dataset SET Restaurant96 = null where Restaurant96 = 99;
UPDATE SIO.dataset SET Restaurant97 = null where Restaurant97 = 99;
UPDATE SIO.dataset SET Restaurant98 = null where Restaurant98 = 99;
UPDATE SIO.dataset SET Restaurant99 = null where Restaurant99 = 99;
UPDATE SIO.dataset SET Restaurant100 = null where Restaurant100 = 99;

