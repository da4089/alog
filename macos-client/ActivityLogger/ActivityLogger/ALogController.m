//
//  ALogController.m
//  ActivityLogger
//
//  Created by David Arnold on 29/03/14.
//  Copyright (c) 2014 David Arnold. All rights reserved.
//

#import "ALogController.h"

@implementation ALogController

- (id)init
{
    self = [super init];
    if (self) {
        // Initialise here
    }
    
    return self;
}


- (void)dealloc
{
    // this is flagged as an issue with ARC: [super dealloc];
}

- (IBAction)cancel:(id) sender
{
    printf("Got cancel.\n");
}

- (IBAction)ok:(id)sender
{
    printf("Got Ok.\n");
}

@end
